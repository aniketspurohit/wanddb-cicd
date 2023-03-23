import wandb
import os

if __name__=="__main__":
  if os.getenv("MY_NAME"):
    print(f"wandb's version: {wandb.__version__}")
