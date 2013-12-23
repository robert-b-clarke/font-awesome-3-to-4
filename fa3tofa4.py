import sys
from fontawesomeupgrader import FontAwesomeUpgrader

#open a file - upgrade font awesome tags then write it back out
html_files = sys.argv[1:]


for html_file in html_files:
    #open file for read
    print ("processing %s " % (html_file))
    fh = open(html_file, 'r')
    html_in = fh.read()
    fh.close
    parser = FontAwesomeUpgrader()
    #get new html
    html_out = parser.process_html(html_in)
    #write the file back out
    fh = open(html_file, 'w')
    fh.write(html_out)
fh.close()
print "done"

