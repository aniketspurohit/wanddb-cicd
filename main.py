import wandb
import os

if __name__=="__main__":
  if (my_name:=os.getenv("MY_NAME")):
    print(f"wandb's version: {wandb.__version__} - {len(my_name)}")
