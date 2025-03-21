import requests, random, json, time, traceback

class UserAgent:
    def __init__(self) -> None:
        self.uaVersions: dict = {
            "chrome": [],
            "firefox": [],
            "edge": []
        }
        r = self.caching('read')
        if r:
            if int(self.uaVersions['ts']) - int(round(time.time())) > 86400:
                self.GetBrowsersVersions()
                self.uaVersions['ts'] = int(round(time.time()))
                self.caching('write')
                del r
        else:
            self.GetBrowsersVersions()
            self.uaVersions['ts'] = int(round(time.time()))
            self.caching('write')
            del r

    def caching(self, req: str):
        try:
            if req == 'write':
                try:
                    with open('ua_versions.json', 'w') as f:
                        json.dump(self.uaVersions, f, ensure_ascii=False, indent=4)
                except:
                    pass

            elif req == 'read':
                try:
                    with open('ua_versions.json', 'r') as f:
                        self.uaVersions = json.load(f)
                        return True
                except:
                    return False
            
        except Exception as err:
            print('Error in caching')
            print(traceback.format_exc())

    def GetBrowsersVersions(self):
        # Chrome latest 3 versions.
        try:
            req = requests.get('https://versionhistory.googleapis.com/v1/chrome/platforms/win/channels/stable/versions')
            if req.status_code == 200:
                c = 0
                for vers in req.json()['versions']:
                    cleaned = vers['version'].split('.')[0] + '.0.0.0'
                    if not cleaned in self.uaVersions['chrome']:
                        c += 1
                        self.uaVersions["chrome"].append(vers['version'].split('.')[0] + '.0.0.0')
                    
                    if c == 3:
                        break
        except Exception as err:
            print('Error in getting Chrome versions')
            print(traceback.format_exc())

        # Firefox latest 3 versions.
        try:
            req = requests.get('https://product-details.mozilla.org/1.0/firefox_history_stability_releases.json')
            if req.status_code == 200:
                biggest = 0
                secondbiggest = 0
                thirdbiggest = 0
                for version in req.json().keys():
                    if int(version.split('.')[0]) > biggest:
                        biggest = int(version.split('.')[0])
                
                for version in req.json().keys():
                    if int(version.split('.')[0]) < biggest and int(version.split('.')[0]) > secondbiggest:
                        secondbiggest = int(version.split('.')[0])
                
                for version in req.json().keys():
                    if int(version.split('.')[0]) < secondbiggest and int(version.split('.')[0]) > thirdbiggest:
                        thirdbiggest = int(version.split('.')[0])
                
                self.uaVersions["firefox"].append(str(biggest) + '.0')
                self.uaVersions["firefox"].append(str(secondbiggest) + '.0')
                self.uaVersions["firefox"].append(str(thirdbiggest) + '.0')
        except Exception as err:
            print('Error in getting Firefox versions')
            print(traceback.format_exc())
    
        # Edge latest verion (as they don't give version history but only the latest)
        try:
            req = requests.get('https://edgeupdates.microsoft.com/api/products')
            if req.status_code == 200:
                for build in req.json():
                    if build['Product'] == 'Stable':
                        self.uaVersions["edge"].append(str(build['Releases'][0]['ProductVersion'].split('.')[0])+'.0.0.0')
                        break
        except Exception as err:
            print('Error in getting Edge versions')
            print(traceback.format_exc())
    
    def genUA(self, amount: int = 1, os: str = 'random', browser: str = 'random', version: str = '0'):
        try:
            UserAgents: list = []
            loop = True
            while loop:
                ua = self.getUA(os, browser, version)
                if ua[0]:
                    UserAgents.append(ua)
                
                if len(UserAgents) == amount:
                    loop = False
                
            return UserAgents
        except Exception as err:
            print('Error in generating UA')
            print(traceback.format_exc())
    
    def getUA(self, os: str = 'random', browser: str = 'random', version: str = '0'):
        try:
            ua: str = ''
            if browser.lower() == 'random':
                loop = True
                while loop:
                    browser = random.choices(list(self.uaVersions.keys()))[0]
                    if not browser.lower() == 'ts':
                        loop = False
            elif not browser.lower() in list(self.uaVersions.keys()):
                return False, 'unsupported browser'
            
            if version == '0':
                version: str = random.choices(self.uaVersions[browser])[0]
            
            if os.lower() == 'random':
                os = random.choices(['win', 'mac', 'linux'])[0]

            if not version in ' '.join(self.uaVersions[browser.lower()]):
                return False, 'unsupported version'
            else:
                if not '.' in version:
                    if browser == 'chrome' or browser == 'edge':
                        version = version+'.0.0.0'
                    elif browser == 'firefox':
                        version = version+'.0'
                    else:
                        return False, 'unsupported version'
            
            if browser.lower() == 'edge' and os.lower() == 'linux':
                return False, 'Edge browser and Linux OS are not yet supported on this script'
            
            if os.lower().startswith('win'):
                if browser == 'chrome':
                    ua += f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.3'
                elif browser == 'edge':
                    ua += f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 Edg/{version}'
                elif browser == 'firefox':
                    ua += f'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{version}) Gecko/20100101 Firefox/{version}'
                else:
                    return False, 'unsupported browser'
            elif os.lower().startswith('mac'):
                if browser == 'chrome':
                    ua += f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.3'
                elif browser == 'edge':
                    ua += f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36 Edg/{version}'
                elif browser == 'firefox':
                    ua += f'Mozilla/5.0 (Macintosh; Intel Mac OS X 14.5; rv:{version}) Gecko/20100101 Firefox/{version}'
                else:
                    return False, 'unsupported browser'
            elif os.lower().startswith('linux'):
                loop = True
                while loop:
                    if browser == 'chrome':
                        ua += f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36'
                        loop = False
                    elif browser == 'firefox':
                        ua += f'Mozilla/5.0 (X11; Linux i686; rv:{version}) Gecko/20100101 Firefox/{version}'
                        loop = False
                    else:
                        browser = random.choices(list(self.uaVersions.keys()))[0]
            else:
                return False, 'unsupported os'
            
            return True, ua, version, browser
        except Exception as err:
            print('Error in getting UA')
            print(traceback.format_exc())

