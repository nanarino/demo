#include <windows.h>
#include <math.h>
#define scale 1.05946309411451
#define note 392.0    // 1=G
#define semibreve 240 // d=60 1/4
typedef short array[];
int main()
{
    short i, j;
    double frequency, octave[12];
    for (i = 0; i < 12; i++)
    {
        octave[i] = note * pow(scale, (double)i);
    }
    /*
        '''python script'''
        import re
        u='                            .                                                                                                               '
        s='35612212331653126661221233561765665322312212362166656612325566663561661232556666356256323312717566356121223121253335665633312122666566123255'
        d='...        ...  ...                          .  ......    ......... ..          ...         . .......                           ......      '

        uta = re.sub(r'(?P<num>\d)', lambda x: ','+str({'0':-1,'1':0,'2':3,'3':5,'4':6,'5':8,'6':9,'7':11,}[x.group("num")]),s)[1:]
        up_index_of = [i.start() for i in re.finditer('\.', u)]
        down_index_of = [i.start() for i in re.finditer('\.', d)]
        print(f'array uta = {{{uta}}};')
        print(f'array {up_index_of=}'.replace('=[',' = {').replace(']','};'))
        print(f'array {down_index_of=}'.replace('=[',' = {').replace(']','};'))
     */

    array uta = {5, 8, 9, 0, 3, 3, 0, 3, 5, 5, 0, 9, 8, 5, 0, 3, 9, 9, 9, 0, 3, 3, 0, 3, 5, 5, 8, 9, 0, 11, 9, 8, 9, 9, 8, 5, 3, 3, 5, 0, 3, 3, 0, 3, 5, 9, 3, 0, 9, 9, 9, 8, 9, 9, 0, 3, 5, 3, 8, 8, 9, 9, 9, 9, 5, 8, 9, 0, 9, 9, 0, 3, 5, 3, 8, 8, 9, 9, 9, 9, 5, 8, 9, 3, 8, 9, 5, 3, 5, 5, 0, 3, 11, 0, 11, 8, 9, 9, 5, 8, 9, 0, 3, 0, 3, 3, 5, 0, 3, 0, 3, 8, 5, 5, 5, 8, 9, 9, 8, 9, 5, 5, 5, 0, 3, 0, 3, 3, 9, 9, 9, 8, 9, 9, 0, 3, 5, 3, 8, 8};
    array up_index_of = {28};
    array down_index_of = {0, 1, 2, 11, 12, 13, 16, 17, 18, 45, 48, 49, 50, 51, 52, 53, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 80, 81, 82, 92, 94, 95, 96, 97, 98, 99, 100, 128, 129, 130, 131, 132, 133};

    for (i = 0; i < 140; i++)
    {
        if (uta[i] == -1)
        {
            Sleep(semibreve);
            continue;
        }
        frequency = octave[uta[i]];
        for (j = 0; j < 1; j++)
        {
            if (i == up_index_of[j])
            {
                frequency *= 2.0;
                break;
            }
        }
        for (j = 0; j < 44; j++)
        {
            if (i == down_index_of[j])
            {
                frequency *= .5;
                break;
            }
        }
        Beep(frequency, semibreve);
    }
    return 0;
}