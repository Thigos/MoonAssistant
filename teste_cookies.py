import browser_cookie3

supported_browsers = [
    browser_cookie3.chrome,
    browser_cookie3.chromium,
    browser_cookie3.opera,
    browser_cookie3.opera_gx,
    browser_cookie3.brave,
    browser_cookie3.edge,
    browser_cookie3.vivaldi,
    browser_cookie3.firefox,
    browser_cookie3.librewolf,
    browser_cookie3.safari,
]

cookie_dict = {}

for browser_fn in supported_browsers:
    try:
        cj = browser_fn(domain_name=".google.com")
        for cookie in cj:
            print(cookie.name)
            if cookie.name == "__Secure-1PSID" and cookie.value.endswith("."):
                cookie_dict["__Secure-1PSID"] = cookie.value
            if True:
                if cookie.name == "__Secure-1PSIDTS":
                    print(cookie.value)
                    cookie_dict["__Secure-1PSIDTS"] = cookie.value
                elif cookie.name == "__Secure-1PSIDCC":
                    print(cookie.value)
                    cookie_dict["__Secure-1PSIDCC"] = cookie.value
            if len(cookie_dict) == 3:
                print(cookie_dict)
    except Exception as e:
        # Ignore exceptions and try the next browser function
        continue

if not cookie_dict:
    raise Exception("No supported browser found or issue with cookie extraction")

print(cookie_dict)