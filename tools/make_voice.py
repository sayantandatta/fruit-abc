"""Generate one British-English MP3 per fruit ("A. Apple.") into docs/audio/.
Runs on GitHub Actions (see .github/workflows/voice.yml). Tries Microsoft's neural
en-GB voice through edge-tts first, then falls back to Piper's offline en_GB voice."""
import asyncio, json, os, subprocess, sys, pathlib, shutil
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs' / 'audio'; OUT.mkdir(parents=True, exist_ok=True)
LINES = json.load(open(ROOT / 'tools' / 'voice-lines.json'))
VOICE = os.environ.get('VOICE', 'en-GB-SoniaNeural')
RATE = os.environ.get('RATE', '-25%')

async def edge():
    import edge_tts
    for ln in LINES:
        mp3 = OUT / f"{ln['id']}.mp3"
        if mp3.exists() and mp3.stat().st_size > 1000: continue
        # A short pause between the letter and the name reads better for a toddler.
        text = f"{ln['letter']}. {ln['name']}."
        await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(mp3))
        print('edge', mp3.name, mp3.stat().st_size)

def piper():
    model = os.environ.get('PIPER_MODEL', 'en_GB-cori-high')
    subprocess.run([sys.executable, '-m', 'piper.download_voices', model], check=True)
    for ln in LINES:
        mp3 = OUT / f"{ln['id']}.mp3"
        if mp3.exists() and mp3.stat().st_size > 1000: continue
        wav = OUT / f"{ln['id']}.wav"
        text = f"{ln['letter']}. {ln['name']}."
        subprocess.run([sys.executable, '-m', 'piper', '-m', model, '--length-scale', '1.25', '--sentence-silence', '0.4', '-f', str(wav)], input=text.encode(), check=True)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(wav), '-codec:a', 'libmp3lame', '-q:a', '4', str(mp3)], check=True)
        wav.unlink(); print('piper', mp3.name, mp3.stat().st_size)

if __name__ == '__main__':
    try:
        asyncio.run(edge()); print('done with edge-tts voice', VOICE)
    except Exception as e:
        print('edge-tts failed:', e, '— falling back to Piper'); piper()
    missing = [ln['id'] for ln in LINES if not (OUT / f"{ln['id']}.mp3").exists()]
    if missing: print('MISSING', missing); sys.exit(1)
    json.dump({ln['name']: f"audio/{ln['id']}.mp3" for ln in LINES}, open(OUT / 'index.json', 'w'), indent=0)
    print(len(LINES), 'clips ready')
