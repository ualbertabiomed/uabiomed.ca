cd v2-website;
npm run export;
cd ../;
rm -rf ./web-bin;
mkdir web-bin
cp -r ./v2-website/__sapper__/export ./web-bin;
sudo python3 server/web.py;
