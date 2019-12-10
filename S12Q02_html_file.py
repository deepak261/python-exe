'''
Write a program that generates a HTML file. 
Prompt the user for webpage title and webpage body contents. 
The webpage body should contain 
    one main header, 
    one sub header, and 
    at least 2 paragraphs.

A sample output is shown below

'''



fh = open('html_file.txt','w')
fh.write('\n')
fh.write('\n')
fh.write('                       webpage.html\n                       ------------')
fh.write('\n')
fh.write('<html>')
fh.write('\n')
fh.write(' <head>')
fh.write('\n')
fh.write('    <title>')
fh.write('\n')
fh.write('          My webpage title')
fh.write('\n')
fh.write('    </title>')
fh.write('\n')
fh.write(' </head>')
fh.write('\n')
fh.write('\n <body>')
fh.write('\n')
fh.write('    <h1>Webpage Banner</h1>')
fh.write('\n')
fh.write('\n    <p>This is a sample story\n       for my first webpage')
fh.write('\n')
fh.write('    </p>')
fh.write('\n')
fh.write('\n    <p>This is a how my sample\n       story ends')
fh.write('\n')
fh.write('    </p>')
fh.write('\n')
fh.write(' </body>')
fh.write('\n')
fh.write('</html>')
fh.write('\n')
fh.write('\n')
fh.write('\n')
fh.write('\n')
fh.close()
      

      

