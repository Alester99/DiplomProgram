INSTRUMENTS = [
    'Acoustic Grand Piano',
    'Bright Acoustic Piano',
    'Electric Grand Piano',
    'Honky-tonk Piano',
    'Electric Piano 1',
    'Electric Piano 2',
    'Harpsichord',
    'Clavi',
    'Celesta',
    'Glockenspiel',
    'Music Box',
    'Vibraphone',
    'Marimba',
    'Xylophone',
    'Tubular Bells',
    'Dulcimer',
    'Drawbar Organ',
    'Percussive Organ',
    'Rock Organ',
    'Church Organ',
    'Reed Organ',
    'Accordion',
    'Harmonica',
    'Tango Accordion',
    'Acoustic Guitar (nylon)',
    'Acoustic Guitar (steel)',
    'Electric Guitar (jazz)',
    'Electric Guitar (clean)',
    'Electric Guitar (muted)',
    'Overdriven Guitar',
    'Distortion Guitar',
    'Guitar harmonics',
    'Acoustic Bass',
    'Electric Bass (finger)',
    'Electric Bass (pick)',
    'Fretless Bass',
    'Slap Bass 1',
    'Slap Bass 2',
    'Synth Bass 1',
    'Synth Bass 2',
    'Violin',
    'Viola',
    'Cello',
    'Contrabass',
    'Tremolo Strings',
    'Pizzicato Strings',
    'Orchestral Harp',
    'Timpani',
    'String Ensemble 1',
    'String Ensemble 2',
    'SynthStrings 1',
    'SynthStrings 2',
    'Choir Aahs',
    'Voice Oohs',
    'Synth Voice',
    'Orchestra Hit',
    'Trumpet',
    'Trombone',
    'Tuba',
    'Muted Trumpet',
    'French Horn',
    'Brass Section',
    'SynthBrass 1',
    'SynthBrass 2',
    'Soprano Sax',
    'Alto Sax',
    'Tenor Sax',
    'Baritone Sax',
    'Oboe',
    'English Horn',
    'Bassoon',
    'Clarinet',
    'Piccolo',
    'Flute',
    'Recorder',
    'Pan Flute',
    'Blown Bottle',
    'Shakuhachi',
    'Whistle',
    'Ocarina',
    'Lead 1 (square)',
    'Lead 2 (sawtooth)',
    'Lead 3 (calliope)',
    'Lead 4 (chiff)',
    'Lead 5 (charang)',
    'Lead 6 (voice)',
    'Lead 7 (fifths)',
    'Lead 8 (bass + lead)',
    'Pad 1 (new age)',
    'Pad 2 (warm)',
    'Pad 3 (polysynth)',
    'Pad 4 (choir)',
    'Pad 5 (bowed)',
    'Pad 6 (metallic)',
    'Pad 7 (halo)',
    'Pad 8 (sweep)',
    'FX 1 (rain)',
    'FX 2 (soundtrack)',
    'FX 3 (crystal)',
    'FX 4 (atmosphere)',
    'FX 5 (brightness)',
    'FX 6 (goblins)',
    'FX 7 (echoes)',
    'FX 8 (sci-fi)',
    'Sitar',
    'Banjo',
    'Shamisen',
    'Koto',
    'Kalimba',
    'Bag pipe',
    'Fiddle',
    'Shanai',
    'Tinkle Bell',
    'Agogo',
    'Steel Drums',
    'Woodblock',
    'Taiko Drum',
    'Melodic Tom',
    'Synth Drum',
    'Reverse Cymbal',
    'Guitar Fret Noise',
    'Breath Noise',
    'Seashore',
    'Bird Tweet',
    'Telephone Ring',
    'Helicopter',
    'Applause',
    'Gunshot'
]
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

errors = {
    'program': 'Bad input, please refer this spec-\n'
               'http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/program_change.htm',
    'notes': 'Bad input, please refer this spec-\n'
             'http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm'
}


def instrument_to_program(instrument: str) -> int:
    assert instrument in INSTRUMENTS, errors['program']
    return INSTRUMENTS.index(instrument) + 1


def program_to_instrument(program: int) ->  str:
    assert 1 <= program <= 128, errors['program']
    return INSTRUMENTS[program - 1]


def number_to_note(number: int) -> tuple:
    octave = number // NOTES_IN_OCTAVE
    assert octave in OCTAVES, errors['notes']
    assert 0 <= number <= 127, errors['notes']
    note = NOTES[number % NOTES_IN_OCTAVE]

    return note, octave


def note_to_number(note: str, octave: int) -> int:
    assert note in NOTES, errors['notes']
    assert octave in OCTAVES, errors['notes']

    note = NOTES.index(note)
    note += (NOTES_IN_OCTAVE * octave)

    assert 0 <= note <= 127, errors['notes']

    return note



midifile = r'C:\Users\Alex\Desktop\MIDI\malaguena.mid'
# with open(midifile, 'rb') as mfile:
#     leader = mfile.read(4)
#     if leader != b'MThd':
#         raise ValueError('Not a MIDI file!')
#     else: print('mfile.read()')#mfile.read()

# import midi
# from midi import ControlChange
# cc = ControlChange(100, 127)
# from midi import Message
# msg = Message(cc, channel=1)
# print(msg.control_number)
# print(msg.value)
#from midi import MidiConnector
#conn = MidiConnector('/dev/serial0', timeout=5)


import mido
melody = []
mid = mido.MidiFile(midifile, clip=True)
#print(mid.__dict__.keys())
#print(mid.tracks__dict__.keys())
for i, track in enumerate(mid.tracks):
    #print('Track {}: {}'.format(i, track.name))
    count = 0
    for msg in track:
        count += 1
        data = msg.__dict__.get('note')
        if type(data) == int: note, octave = number_to_note(data); melody.append(str(note)+str(octave)); #print(count,')',"|",data,"|",note,"|", octave )
        #else: print(count,')',msg)
track = len(mid.tracks)
#print('info',mid.tracks, track)
print(melody)
#print('--------------',mid.print_tracks(),'--------------')

# for m in mid.tracks[0]:
#     print(m, type(m))

# def msg2dict(msg):
#     result = dict()
#     if 'note_on' in msg:
#         on_ = True
#     elif 'note_off' in msg:
#         on_ = False
#     else:
#         on_ = None
#     result['time'] = int(msg[msg.rfind('time'):].split(' ')[0].split('=')[1].translate(
#         str.maketrans({a: None for a in string.punctuation})))

#     if on_ is not None:
#         for k in ['note', 'velocity']:
#             result[k] = int(msg[msg.rfind(k):].split(' ')[0].split('=')[1].translate(
#                 str.maketrans({a: None for a in string.punctuation})))
#     return [result, on_]

# for m in mid.tracks[0]:
#     print(m,msg2dict(m),"----------------------")

# with mido.open_input() as inport:
#     for msg in inport:
#         print(msg)

# mid = mido.MidiFile(midifile)
# for msg in mid.play():
#     port.send(msg)

# msg = mido.Message('note_on', note=60)
# msg.type
# msg.note
# msg.bytes()
# msg.copy(channel=2)

# print(msg.note,type(msg))

Notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
count_of_frets = 25
count_of_strings = 6
d = 1
e = 0.5

def PrintMas(a):
    print()
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()
    print()

def res (number):
    if number == 11: return 0
    else: return number+1

def CreateStringsFrets(Notes):
    StringsFrets = []
    for i in range(count_of_strings):
        StringsFrets.append([])
        if i == 0: number = 7; octava = 2
        elif 'C' != StringsFrets[i-1][5][:len(StringsFrets[i-1][5])-1]:  mystr = StringsFrets[i-1][5]; number = Notes.index(mystr[:len(mystr)-1]); octava = int(mystr[len(mystr)-1])
        else: mystr = StringsFrets[i-1][4]; number = Notes.index(mystr[:len(mystr)-1]); octava = int(mystr[len(mystr)-1])
        for j in range(count_of_frets):
            N = ''
            StringsFrets[i].append(Notes[number]+ str(octava))
            if number == 2: octava += 1
            number = res(number)
    PrintMas(StringsFrets)
    return StringsFrets 
StringsFrets = CreateStringsFrets(Notes)

def GetListOfNotes(StringsFrets):
    ListOfNotes = []
    for i in range(count_of_strings):
        for j in range(count_of_frets):
            ListOfNotes.append(StringsFrets[i][j])
    ListOfNotes = set(ListOfNotes)
    ListOfNotes = list(ListOfNotes)
    #print('\n',ListOfNotes,'\n')
    return ListOfNotes

ListOfNotes = GetListOfNotes(StringsFrets)

def StringsFretsForNote (StringsFrets, ListOfNotes):
    Note_S_F=[]
    # count_of_frets = 25
    # count_of_strings = 6
    for k in range(len(ListOfNotes)):
        Note_S_F.append([])
        Note_S_F[k].append(ListOfNotes[k]) #; print(ListOfNotes[k])
        for i in range(count_of_strings):
            for j in range(count_of_frets):
                if ListOfNotes[k] == StringsFrets[i][j]: Note_S_F[k].append({'s':i,'f':j})#; print(i,j)
    #PrintMas(Note_S_F)
    return Note_S_F

Note_S_F = StringsFretsForNote (StringsFrets, ListOfNotes)


def g (xt1,xt):
    #print(xt1,xt,d**2*(2**(-xt.get('f')/12)-2**(-xt1.get('f')/12))**2,e**2*(xt.get('s')-xt1.get('s'))**2)
    return d**2*(2**(-xt.get('f')/12)-2**(-xt1.get('f')/12))**2+e**2*(xt.get('s')-xt1.get('s'))**2

def MelodyToTable (melody,Note_S_F):
    MelodyToTable = []
    for i in range (len(melody)):
        MelodyToTable.append([])
        for j in range (len(Note_S_F)):
            if melody[i] == Note_S_F[j][0]:
                for k in range(1,len(Note_S_F[j])):
                    MelodyToTable[i].append(Note_S_F[j][k])
    PrintMas(MelodyToTable)
    return MelodyToTable

MelodyToTable = MelodyToTable (melody,Note_S_F)        
def countf (MelodyToTable,i,j,F):
    mas = []
    for k in range (len(MelodyToTable[i-1])):
        #print(F[0][j],g(MelodyToTable[i-1][k],MelodyToTable[i][j]))
        mas.append(F[i-1][k]+g(MelodyToTable[i-1][k],MelodyToTable[i][j])) #
    #print(mas,min(mas))
    return min(mas)

# countf (MelodyToTable,1,0,[],[[0], [0], [0], [0], [0], [0]])     

#print(g(Note_S_F[0][1],Note_S_F[4][2]))

def f (MelodyToTable):
    F = []
    for i in range (len(MelodyToTable)):
        F.append([])
        for j in range (len(MelodyToTable[i])):
            if i == 0: F[i].append(0)
            else: F[i].append(countf(MelodyToTable,i,j,F))
    PrintMas(F)
    return F, F[len(F)-1].index(min(F[len(F)-1]))
F, x = f (MelodyToTable)

def Tabulature (MelodyToTable,F):
    T = []
    F = F[::-1];MelodyToTable=MelodyToTable[::-1]
    for i in range(len(F)):
        mas = []
        for j in range (len(F[i])):
            if i == 0: mas.append(F[i].index(min(F[i])))
            else: mas.append(g(MelodyToTable[i][j],MelodyToTable[i-1][T[i-1]])+F[i][j])
        T.append(mas.index(min(mas))) 
    MelodyToTable = MelodyToTable[::-1]; T=T[::-1]  
    FinalT = []
    for i in range (len(T)):
        FinalT.append(MelodyToTable[i][T[i]])
    print(FinalT)
    return (FinalT)

FinalT = Tabulature (MelodyToTable,F)
def TabulatureToNotes (FinalT,StringsFrets,melody):
    ShowNotes = []
    PrintMas(StringsFrets)
    for i in range(len(FinalT)):
        ShowNotes.append(StringsFrets[FinalT[i].get('s')][FinalT[i].get('f')])
    print (ShowNotes)
    if ShowNotes == melody: print ("ShowNotes == melody")
TabulatureToNotes (FinalT,StringsFrets,melody)        

