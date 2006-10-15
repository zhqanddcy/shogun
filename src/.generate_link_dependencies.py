import os,re,sys

incexpr=re.compile('^\s*[%#]include "(\S+)"',re.MULTILINE)
deps=dict();
deps['carrays.i']=[]
deps['cpointer.i']=[]

initial_deps=deps.copy()


def get_deps(f):
	global deps
	global fdep
	try:
		for d in deps[f]:
			if d not in fdep:
				fdep+=[d]
				get_deps(d)
				cppfile=d[:-1]+'cpp'

				if cppfile not in fdep and deps.has_key(cppfile):
					fdep+=[cppfile]
					get_deps(cppfile)
	except KeyError:
		print >>sys.stderr, "generate_link_dependencies: warning: could not find dependencies for '%s'" % f 

#scan each file for potential includes
files=sys.stdin.readlines()
for f in files:
	f=f[:-1]
	deps[f]=re.findall(incexpr, file(f).read())

#generate linker dependencies
for f in deps.iterkeys():
	if f[-1] == 'i' and not initial_deps.has_key(f):
		str1=os.path.join(os.path.dirname(f), '_' + os.path.basename(f)[:-2]) + '.so: ' + f[:-2]+'_wrap.cxx.o'
		str2=os.path.join(os.path.dirname(f), os.path.basename(f)[:-2]) + '_wrap.cxx: ' + f


		fdep=list();
		get_deps(f)
		for d in fdep:
			if d[-4:]=='.cpp' or d[-2:]=='.c':
				str1+=' ' + d + '.o'
			if d[-2:]=='.h' or d[-2:]=='.i':
				str2+=' ' + d 

		print str1
		print str2
