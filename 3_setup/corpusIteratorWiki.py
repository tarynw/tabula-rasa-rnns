from paths import WIKIPEDIA_HOME
import random
 
# modified to switch shuffling to False (Gulordava materials already shuffled at sentence level)
def load(language, partition, doShuffling=False):
  # modifying code to track train sets from Gulordava study
  if language in ["Italian", "German", "English","Russian"]:
    chunks = []
    with open(WIKIPEDIA_HOME+"/"+language+"/"+partition".txt", "rb") as inFile:
      for line in inFile:
        line = line.decode('utf8')
        chunks.append(line.strip().lower())
        if len(chunks) > 20000:
           if doShuffling:
              random.shuffle(chunks)
           yield "".join(chunks)
           chunks = []
    yield "".join(chunks)
  

def training(language):
  return load(language, "train")

def dev(language, doShuffling=False):
  return load(language, "valid", doShuffling=doShuffling)