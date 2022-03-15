import webbrowser

def main():
    websites = {"google", "twitter", "instagram", "facebook"}
    webbrowser.open(f"http://www.{websites.pop()}.com", new=2)


main()