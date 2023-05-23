if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/beereshpkambali/Mr_Abnormal_Pvt_Bot.git /Abnormal
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Abnormal
fi
cd /Abnormal 
pip3 install -U -r requirements.txt
echo "Starting 𝗠𝗿 𝗔𝗯𝗻𝗼𝗿𝗺𝗮𝗹 𝗣𝗥𝗢 𝗕𝗢𝗧....🔥"
python3 bot.py
