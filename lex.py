import ply.lex as lex
import pyarabic.araby as araby
import pyarabic.number as number
import ply.yacc as yacc
import sys
import arabic_reshaper
import bidi.algorithm

tokens = [
    'bassmala',
    'issmj1',
    'issmj2',
    'sifa',
    'sifa2',
    '7arf3atf',
    'damir',
    'moubtada2',
    '7arfjazm',
    'moudari31',
    '7arfjar4',
    'khabar',
    'issm',
    'moudari32',
    'mad',
    'fi3lamr',
    'a3oudou',
    '7arfjar1',
    'rabi',
    'moudafilayh',
    '7arfjar2',
    'ismmbm',
    'ismmawsoul',
    'fi3lmad',
    'modaf1',
    'modaf2',
    'modaf3',
    'darfzaman',
    'fi3l2',
    'modaf22',
    '7arfjar3',
    'ismajrour2',
    'INT'] 
#t_lettre = u'[أ-ي]'
t_bassmala=u'(بِسْمِ)'
t_issmj1=u'(اللَّهِ)'
t_issmj2=u'(اللَّهُ)'
t_sifa=u'(الرَّحْمَانِ)'
t_sifa2=u'(الرَّحِيمِ)'
t_damir=u'(هُوَ)'
t_7arf3atf = u'(وَ)'
t_moubtada2=u'( الصَّمَدُ)'
t_7arfjazm=u'(لَمْ)'
t_moudari31=u'(يَكُن)'
t_7arfjar4= u'(لَّهُۥ)'
t_khabar= u'(كُفُوًا)'
t_issm= u'(أَحَدٌ)'
t_moudari32=u'(يَلِدْ)'
t_mad=u'(يُولَدْ)'
t_fi3lamr=u'(قُلْ)'
t_a3oudou=u'(أَعُوذُ)'
t_7arfjar1=u'(بِ)'
t_rabi=u'(رَبِّ)'
t_moudafilayh=u'(ٱلْفَلَقِ)'
t_7arfjar2=u'(مِن)'
t_ismmbm=u'(شَرِّ)'
t_ismmawsoul=u'(مَا)'
t_fi3lmad=u'(خَلَقَ)'
t_modaf1=u'(غَاسِقٍ)'
t_modaf2=u'(حَاسِدٍ)'
t_modaf3=u'(حَسَدَ)'
t_darfzaman=u'(إِذَا)'
t_fi3l2=u'(وَقَبَ)'
t_modaf22=u'(ٱلنَّفَّـاثَـاتِ)'
t_7arfjar3=u'(فِى)'
t_ismajrour2=u'(ٱلْعُقَدِ)'
t_ignore = r' \t'
t_INT = r'\([0-9]\)'
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lex.lex()
data = "بسم الله الرحمان الرحيم قل هو الله أحد(1)الله الصمد(2)لم يلد و لم يولد(3)و لم يكن له كفؤا أحد(4)" 
#data = "قل أعوذ برب الفلق(1) من شر ما خلق(2)و من شر غاسق إذا وقب(3)و من شر النفاثات في العقد(4) من شر حاسد إذا حسد(5)"
lex.input(data)

#while 1:
#    tok = lex.token()
#   if not tok:
#        break
#   print(tok)
