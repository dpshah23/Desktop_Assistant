import psutil

def get_user_installed_apps():
    exclude_processes = ["System", "svchost.exe", "conhost.exe", "explorer.exe", "RuntimeBroker.exe", "dllhost.exe", "csrss.exe", "msedge.exe", "chrome.exe", "python.exe"]
    
    processes = [p.info['name'] for p in psutil.process_iter(['pid', 'name']) if p.info['name'] not in exclude_processes]
    return processes


user_installed_apps = get_user_installed_apps()

if user_installed_apps:
        for app in user_installed_apps:
            print(app.replace('.exe', ''))
else:
        print("No user-installed applications found.")