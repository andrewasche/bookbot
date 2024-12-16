import re

def get_character_counts( contents ):
    prog = re.compile("[a-z]")
    contents = contents.lower()
    character_counts = {}
    for character in contents:
        if not prog.match(character):
            continue;

        if character not in character_counts:
            character_counts[character] = 0;
        character_counts[character] += 1

    return character_counts;


filename = "books/frankenstein.txt";

with open(filename) as f:
    file_contents = f.read();
    print("--- Begin report of "+filename+" ---");
    print( str(len( file_contents.split() ) ) + " words found in the document"  );
    print( "" )

    char_counts = get_character_counts( file_contents )
    sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1]))

    sorted_char_counts_keys = list( sorted_char_counts.keys() );
    for a in range( len( sorted_char_counts ) -1, -1, -1):
        print( "The '"+sorted_char_counts_keys[a]+"' character was found "+ str(sorted_char_counts[sorted_char_counts_keys[a]])+" times" )


    print("--- End report ---");

