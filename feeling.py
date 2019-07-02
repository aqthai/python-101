#
#Author: Alvin Thai
#Description:
#   Prints lyrics to "I got this feeling" by JT
#
def print_verse_a():
    print("I got this feeling inside my bones\nIt goes electric, wavey when I turn it on\nAll through my city, all through my home\nWe're flying up, no ceiling, when we in our zone\n")
    
def print_verse_b():
    print("I got that sunshine in my pocket\nGot that good soul in my feet\nI feel that hot blood in my body when it drops\nI can't take my eyes up off it, moving so phenomenally\nRoom on lock, the way we rock it, so don't stop\n")
    
def print_verse_c():
    print("Ooh, it's something magical\nIt's in the air, it's in my blood, it's rushing on\nI don't need no reason, don't need control\nI fly so high, no ceiling, when I'm in my zone\n")
    
def print_pre_chorus():
    print("And under the lights when everything goes\nNowhere to hide when I'm getting you close\nWhen we move, well, you already know\nSo just imagine, just imagine, just imagine\n")
    
def print_chorus():
    print("Nothing I can see but you when you dance, dance, dance\nA feeling good, good, creeping up on you\nSo just dance, dance, dance, come on\nAll those things I shouldn't do\nBut you dance, dance, dance\nAnd ain't nobody leaving soon, so keep dancing\n")
    
def print_post_chorus():
    print("I can't stop the feeling\nSo just dance, dance, dance\nI can't stop the feeling\nSo just dance, dance, dance\n")
    
def print_bridge():
    print("I can't stop the, I can't stop the\nI can't stop the, I can't stop the\nI can't stop the feeling\n")
    
def print_song():
    print_verse_a()
    print_verse_b()
    print_pre_chorus()
    print_chorus()
    print_post_chorus()
    print_verse_c()
    print_verse_b()
    print_pre_chorus()
    print_chorus()
    print_post_chorus()
    print_post_chorus()
    print_bridge()
    print_chorus()
    
def print_remix():
    print_verse_b()
    print_chorus()
    print_post_chorus()
    print_verse_b()
    print_verse_b()
    print_chorus()
    print_post_chorus()
    print_verse_b()
    print_verse_b()
    print_verse_b()
    print_chorus()
    print_post_chorus()
    
def main():
    print_song()
    print()
    print_remix()
main()

