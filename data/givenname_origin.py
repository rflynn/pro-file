#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
map given/first name to hints
"""

import hint
import names

GivenNames = (

# Name,(Hint),(NickNames)

('MOHAMAD','REL.MUSLIM',()),
('MOHAMED','REL.MUSLIM',()),
('MOHAMMAD','REL.MUSLIM',()),
('MOHAMMADI','REL.MUSLIM',()),
('MOHAMMED','REL.MUSLIM',()),

# Jesus and Family and Twelve Apostles
('JESÚS','REL.CHRISTIAN',()),
('MARY','REL.CHRISTIAN',()),
('PETER',('REL.CHRISTIAN','CC.EN','CC.DE','CC.NL','REG.SCAN','CC.SI','CC.SK'),'PETE'),
('JAMES',('REL.CHRISTIAN','CC.EN'),('JIM','JIMMY')),
('JOHN',('REL.CHRISTIAN','CC.EN'),('JACK','JOHNNY')),
('ANDREW',('REL.CHRISTIAN','CC.EN'),'DREW'),
('PHILIP',('REL.CHRISTIAN','CC.EN','REG.SCAN','CC.NL'),('PHIL','PHILLIP')),
('BARTHOLOMEW','REL.CHRISTIAN','BART'),
('MATTHEW',('REL.CHRISTIAN','CC.EN'),'MATT'),
('THOMAS','REL.CHRISTIAN','TOM'),
('JUDE','REL.CHRISTIAN',()),
('SIMON','REL.CHRISTIAN',()),
('MATTHIAS','REL.CHRISTIAN','MATT'),

# Christian Archangels
('MICHAEL','REL.CHRISTIAN','MIKE'),
('MICK',('REL.CHRISTIAN','CC.IN'),()),
('GABRIEL','REL.CHRISTIAN',()),
('RAPHAEL','REL.CHRISTIAN',()),

('ROBERT',('CC.EN','CC.FR','REG.SCAN','CC.DE','CC.NL','CC.CZ','CC.PL','CC.RU','CC.SI','CC.HR','CC.RO'),('BOB','BOBBY')),
('ROBERTO','CC.IT',()),
('ROBERTA','CC.IT',()),

# Top U.S. given names according to U.S. Census 1900-2010
# Categorization Source: http://www.behindthename.com/
('WILLIAM','CC.EN',('BILL','BILLY')),
('DAVID',('REL.BIBLE.OLD','REL.BIBLE.NEW','REG.EUROPE'),'DAVE'),
('RICHARD',('CC.EN','CC.FR','CC.DE','CC.CZ','CC.NL'),('RICK','RICH')),
('CHARLES',('CC.EN','CC.FR'),'CHUCK'),
('JOSEPH',('CC.EN','CC.FR','CC.DE','REL.BIBLE.OLD','REL.BIBLE.NEW'),'JOE'),
('THOMAS',('CC.EN','CC.FR','CC.DE','REG.SCAN','CC.GR','REL.BIBLE.NEW'),()),
('PATRICIA',('CC.EN','CC.ES','CC.DE'),'PAT'),
('PATRICK',('CC.EN','CC.ES','CC.DE'),'PAT'),
('GEORGE',('CC.EN','CC.RO'),()),
('BARBARA',('CC.EN','CC.IT','CC.DE','CC.PL','CC.HU','CC.SI','REL.BIBLE.NEW'),()),
('DONALD',('CC.ST','CC.EN'),('DON','DONNY','DONNIE')),
('DOROTHY','CC.EN',('DOT','DOTTY')),
('LINDA',('CC.EN','CC.NL','REG.SCAN','CC.FI','CC.IT','CC.HU','CC.SK','CC.BG'),()),
('MARGARET','CC.EN','MAGGIE'),
('ELIZABETH',('CC.EN','REL.BIBLE.NEW'),('LIZ','BETH','BETTY','LISA')),
('DANIEL',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.FR','CC.DE','REG.SCAN','CC.PL','CC.ES','CC.PT','CC.RO','CC.SI'),('DAN','DANNY')),
('PAUL',('REL.BIBLE.NEW','CC.EN','CC.FR','CC.DE','CC.NL','REG.SCAN'),()),
('CHRISTOPHER',('REL.BIBLE.NEW','CC.EN'),'CHRIS'),
('EDWARD',('CC.EN','CC.PL'),('ED','EDDIE')),
('HELEN','CC.EN',()),
('KENNETH',('CC.ST','CC.EN','REG.SCAN'),('KEN','KENNY')),
('MARK',('CC.EN','CC.RU','CC.NL','REG.SCAN','REL.BIBLE.NEW'),()),
('ANTHONY','CC.EN','TONY'),
('RONALD',('CC.ST','CC.EN'),('RON','RONNY','RONNIE')),
('SUSAN','CC.EN','SUE'),
('SUSANNA',('CC.IT','CC.SE','CC.FI','CC.RU','CC.NL','CC.EN','REL.BIBLE.NEW'),('SUSAN','SUSANNAH')),
('JENNIFER','CC.EN',('JEN','JENNY')),
('STEVEN','CC.EN','STEVE'),
('RUTH',('CC.EN','CC.DE','REG.SCAN','REL.BIBLE.OLD','REL.BIBLE.NEW'),()),
('NANCY','CC.EN',()),
('FRANK',('CC.EN','CC.DE','CC.NL','CC.FR'),()),
('KAREN',('CC.DA','CC.NO','CC.DE','CC.EN'),()),
('CAROL','CC.EN',()),
('BRIAN',('CC.IE','CC.EN'),()),
('GARY','CC.EN',()),
('SANDRA',('CC.IT','CC.EN','CC.FR','CC.PT','CC.DE','CC.NL','REG.SCAN','CC.FI','CC.LV','CC.SI','CC.MK'),()),
('KEVIN',('CC.EN','CC.IE','CC.FR','CC.DE','CC.NL','REG.SCAN'),()),
('ANNA',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.IT','CC.DE','CC.NL','REG.SCAN','CC.FI','CC.ES','CC.GR','CC.HU','CC.PL','CC.RU','CC.CZ','CC.SK','CC.IS'),()),
('TIMOTHY',('CC.EN','REL.BIBLE.NEW'),'TIM'),
('RAYMOND',('CC.EN','CC.FR'),'RAY'),
('DONNA','CC.EN',()),
('SHIRLEY','CC.EN',()),
('SARAH',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.FR','CC.DE'),()),
('LAURENCE','CC.EN','LARRY'),
('VIRGINIA',('CC.EN','CC.IT','CC.ES','CC.PT','CC.SE','CC.RO',),()),
('JEFFREY','CC.EN','JEFF'),
('LISA',('CC.EN','CC.DE','CC.NL','REG.SCAN','CC.IT'),()),
('STEPHEN',('CC.EN','REL.BIBLE.NEW'),'STEVE'),
('FRANCES','CC.EN',()),
('JOSHUA',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN'),'JOSH'),
('SHARON',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN'),()),
('WALTER',('CC.EN','CC.DE','REG.SCAN','CC.PL','CC.IT'),('WALT','WALLY')),
('KATHLEEN',('CC.EN','CC.EN'),'KATHY'),
('JASON',('CC.EN','CC.FR','REL.BIBLE.NEW','CC.GR'),()),
('WILLIE','ETH.BLACK','WILL'),
('DEBORAH',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN'),('DEBBIE','DEB','DEBRA')),
('JESSICA','CC.EN','JESS'),
('LAURA',('CC.EN','CC.ES','CC.IT','CC.PT','CC.RO','CC.FI','CC.EE','CC.HU','CC.PL','CC.SI','REG.SCAN','CC.DE','CC.NL'),()),
('HAROLD','CC.EN','HARRY'),
('CATHERINE',('CC.FR','CC.EN'),'CATHY'),
('JACK','CC.EN',()),
('HENRY','CC.EN',()),
('ALICE',('CC.EN','CC.FR','CC.PT','CC.IT',),()),
('MARIE',('CC.FR','CC.CZ','CC.DE','CC.EN','REG.SCAN'),()),
('JEREMY',('CC.EN','REL.BIBLE.NEW'),'JERRY'),
('GERALD',('CC.EN','CC.DE'),'JERRY'),
('ERIC',('CC.EN','CC.FR','CC.SE'),()),
('CYNTHIA','CC.EN',()),
('MILDRED','CC.EN',()),
('MARTHA',('CC.EN','REG.SCAN','REL.BIBLE.NEW','CC.GR'),()),
('SCOTT',('CC.EN','CC.ST'),()),
('KIMBERLY','CC.EN',()),
('EVELYN',('CC.EN','CC.DE'),()),
('DENNIS',('CC.EN','CC.DE','CC.NL'),()),
('DORIS',('CC.EN','CC.DE'),()),
('MICHELLE',('CC.FR','CC.EN','CC.NL'),()),
('REBECCA',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.IT','CC.SE'),()),
('ARTHUR',('CC.EN','CC.FR','CC.DE','CC.NL'),'ART'),
('GREGORY','CC.EN','GREG'),
('CAROLYN','CC.EN',()),
('JANE','CC.EN',('JANET','JANICE')),
('NICHOLAS',('CC.EN','CC.FR','CC.NL','CC.RU'),'NICK'),
('JEAN',('CC.FR','CC.EN','CC.ST'),()),
('JOYCE','CC.EN','JOY'),
('RYAN',('CC.IE','CC.EN'),()),
('JOAN',('CC.EN','CC.ES','ETH.CATALAN'),()),
('BRENDA','CC.EN',()),
('SAMUEL',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.FR','CC.ES','CC.PT','CC.PL','CC.CZ','CC.SK','REG.SCAN','CC.FI'),'SAM'),
('ROSE',('CC.EN','CC.FR'),()),
('ALBERT',('CC.EN','CC.FR','CC.SI','CC.PL','CC.RU','CC.NL','REG.SCAN'),'AL'),
('CARL',('CC.DE','REG.SCAN','CC.EN'),()),
('PAMELA','CC.EN','PAM'),
('MELISSA',('CC.EN','CC.NL'),()),
('PATRICK',('CC.IE','CC.EN','CC.FR','CC.DE'),()),
('KATHERINE','CC.EN',('KAT','KATHY')),
('AMANDA',('CC.EN','CC.ES','CC.PT','CC.IT','REG.SCAN','CC.NL','CC.DE','CC.FI',),()),
('ASHLEY','CC.EN',()),
('STEPHANIE',('CC.EN','CC.DE'),()),
('CHRISTINE',('CC.FR','CC.EN','CC.DE','REG.SCAN','CC.NL',),()),
('JONATHAN',('CC.EN','CC.DE','REG.SCAN','CC.NL'),'JON'),
('DOUGLAS',('CC.ST','CC.EN'),'DOUG'),
('EMILY','CC.EN',()),
('ANN','CC.EN',()),
('AMY','CC.EN',()),
('ANGELA',('CC.EN','CC.IT','CC.DE','CC.RO','CC.SI','CC.SK','CC.RU','CC.MK'),()),
('DIANE',('CC.FR','CC.EN'),()),
('JOE','CC.EN',()),
('JACOB',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.NL','REG.SCAN'),()),
('LAURENCE','CC.EN','LAWRENCE'),
('RALPH',('CC.EN','REG.SCAN','CC.DE'),()),
('JUDITH',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.FR','CC.DE','CC.ES'),'JUDY'),
('JUSTIN',('CC.EN','CC.FR','CC.SI'),()),
('TERRY','CC.EN',()),
('BENJAMIN',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.FR','CC.DE'),'BEN'),
('BRANDON','CC.EN',()),
('GLORIA',('CC.IT','CC.ES','CC.PT','CC.EN'),()),
('ROY',('CC.ST','CC.EN','CC.NL'),()),
('ROGER',('CC.EN','CC.FR','CC.DE','CC.SE'),()),
('LILLIAN','CC.EN','LILLY'),
('EUGENE','CC.EN',()),
('MARIA',('CC.IT','CC.PT','ETH.CATALAN','CC.DE','REG.SCAN','ETH.FRISIAN','CC.GR','CC.PL','CC.RO','CC.FI','CC.IS','ETH.CORSICAN','ETH.BASQUE'),()),
('IRENE',('CC.EN','CC.IT','CC.ES','CC.PT','REG.SCAN','CC.FI','CC.DE'),()),
('LOUIS',('CC.FR','CC.EN','CC.NL'),('LOU','LOUIE')),
('LOIS',('CC.EN','ETH.GALICIAN'),()),
('LOUISE',('CC.FR','CC.EN','CC.NL'),()),
('KATHRYN','CC.EN',()),
('FLORENCE',('CC.EN','CC.FR'),()),
('GRACE','CC.EN',()),
('BEVERLY','CC.EN',()),
('JULIE',('CC.FR','CC.EN'),()),
('EMMA',('CC.EN','CC.FR','CC.IT','CC.NL','CC.DE'),()),
('KELLY',('CC.IE','CC.EN'),()),
('MARILYN','CC.EN',()),
('HOWARD','CC.EN',()),
('CHERYL','CC.EN',()),
('RACHEL',('CC.EN','REL.BIBLE.OLD','REL.BIBLE.NEW','CC.FR','CC.DE'),()),
('THERESA',('CC.EN','CC.DE','REG.SCAN'),()),
('JUDY','CC.EN',()),
('RUBY','CC.EN',()),
('ANNIE','CC.EN',()),
('FRED',('CC.EN','CC.NL'),()),
('JULIA',('CC.EN','CC.DE','REG.SCAN','CC.NL','CC.ES','CC.PT','CC.FI','REL.BIBLE.NEW',),()),
('PHYLLIS',('CC.EN','CC.DE'),()),
('NICOLE',('CC.FR','CC.EN','CC.NL'),()),
('JOSÉ',('CC.ES','CC.PT'),()),
('BRUCE',('CC.ST','CC.EN'),()),
('ALEXANDER',('CC.EN','CC.DE','CC.NL','REG.SCAN','CC.HU','CC.SK','MYTH.GREEK'),()),
('HEATHER','CC.EN',()),
('KEITH',('CC.EN','CC.ST'),()),
('EDNA',('CC.IE','CC.ST','CC.EN','REL.BIBLE.OLD'),()),
('WAYNE','CC.EN',()),
('TERESA',('CC.ES','CC.PT','CC.IT','CC.FI','CC.PL','CC.DE','REG.SCAN','CC.EN'),()),
('FRANCIS',('CC.EN','CC.FR'),()),
('AARON',('REL.BIBLE.OLD','CC.EN',),()),
('JACQUELINE',('CC.FR','CC.EN'),()),
('GLADYS',('CC.CY','CC.EN'),()),
('CLARENCE','CC.EN',()),
('RUSSELL','CC.EN',()),
('MARJORIE','CC.EN',()),
('ADAM',('REL.BIBLE.OLD','REL.BIBLE.NEW','CC.EN','CC.FR','CC.DE','CC.NL','CC.PL','CC.CZ','CC.RU','CC.UA','CC.HR','CC.MK','CC.RO','LANG.ARABIC'),()),
('JOSEPHINE',('CC.EN','CC.DE'),()),
('BONNIE','CC.EN',()),
('CHRISTINA',('CC.EN','CC.DE','REG.SCAN','CC.NL','REL.BIBLE.NEW'),()),
('EARL','CC.EN',()),
('ETHEL','CC.EN',()),
('STANLEY','CC.EN',()),
('ERNEST',('CC.EN','CC.FR','CC.SI'),()),
('ANNE',('CC.FR','CC.EN','REG.SCAN','CC.FI','CC.DE','CC.NL','ETH.BASQUE','ETH.FRISIAN'),()),
('JESSE',('CC.EN','CC.NL','REL.BIBLE.OLD','REL.BIBLE.NEW'),()),
('TYLER','CC.EN',()),
('SARA',('CC.GR','CC.ES','CC.IT','REG.SCAN','CC.DE','CC.NL','CC.SI','CC.MK','CC.PL','CC.EN','LANG.ARABIC'),()),
('LEONARD',('CC.EN','CC.PL'),()),
('NORMA',('CC.EN','CC.IT'),()),
('VICTORIA',('CC.EN','CC.ES','CC.RO','MYTH.ROMAN'),()),
('ELEANOR','CC.EN',()),
('LESLIE','CC.EN',()),
('SAMANTHA',('CC.EN','CC.IT','CC.NL'),()),
('MARION',('CC.FR','CC.EN'),()),
('BOBBY','CC.EN',()),
('RITA',('CC.IT','CC.EN','REG.SCAN','CC.DE','CC.HU','CC.ES','CC.PT',),()),
('NATHAN',('CC.EN','CC.FR','REL.BIBLE.OLD'),()),
('PEGGY','CC.EN','PEG'),
('EDITH',('CC.EN','CC.DE','REG.SCAN','CC.NL'),()),
('DENISE',('CC.FR','CC.EN','CC.NL'),()),
('THELMA','CC.EN',()),
('WANDA',('CC.PL','CC.EN','CC.DE','CC.FR'),()),
('KATHY','CC.EN',()),
('DALE','CC.EN',()),
('ANDREA',('CC.IT','CC.EN','CC.DE','CC.CZ','CC.HU','REG.SCAN','CC.HR'),()),
('ANDRÉA',('CC.BR','LANG.PORTUGUESE.BRAZIL'),()),
('KYLE','CC.EN',()),
('ZACHARY','CC.EN',()),
('DIANA',('CC.EN','CC.ES','CC.IT','CC.PT','ETH.CATALAN','CC.DE','CC.NL','CC.RU','CC.LT','MYTH.ROMAN'),()),
('HAZEL','CC.EN',()),
('NORMAN','CC.EN',()),
('LEE','CC.EN',()),
('ALAN',('CC.EN','CC.ST','ETH.BRETON'),()),
('PAULINE',('CC.FR','CC.EN','CC.DE','REG.SCAN'),()),
('LUCILLE',('CC.FR','CC.EN'),()),
('CHARLOTTE',('CC.FR','CC.EN','CC.DE','REG.SCAN','CC.NL'),()),
('LAUREN','CC.EN',()),
('ESTHER',('CC.EN','CC.FR','CC.ES','CC.NL','REL.BIBLE.OLD'),()),
('JESSIE',('CC.ST','CC.EN'),()),
('CLARA',('CC.IT','CC.DE','CC.ES','CC.PT','ETH.CATALAN','CC.RO','CC.EN'),()),
('ELLEN',('CC.EN','CC.NL'),()),
('JEREMY',('CC.EN','REL.BIBLE.NEW'),()),
('VINCENT',('CC.EN','CC.FR','CC.NL','CC.DA','CC.SE','CC.SK'),'VINCE'),
('ROBIN',('CC.EN','CC.NL','CC.SE'),()),
('MARTIN',('CC.EN','CC.FR','CC.DE','REG.SCAN','CC.RU','CC.RO','CC.CZ','CC.SK','CC.HR','CC.HU','CC.BG','CC.FI'),'MARTY'),
('LORI','CC.EN',()),
('RANDALL','CC.EN','RANDY'),
('ELAINE',('CC.EN','CC.CY'),()),
('ALFRED',('CC.EN','CC.FR','REG.SCAN','CC.DE','CC.PL','CC.NL'),'AL'),
('HERBERT',('CC.EN','CC.DE','CC.FR','CC.SI','CC.PL'),('HERB','BERT')),
('MEGAN',('CC.CY','CC.EN'),'MEG'),
('SEÁN','CC.IE',()),
('SEAN',('CC.IE','CC.EN'),'SHAWN'),
('FREDERICK','CC.EN','FRED'),
('MELVIN','CC.EN',()),
('MARVIN',('CC.EN','CC.DE'),()),
('CONNIE','CC.EN',()),
('TAMMY','CC.EN',()),
('JORDAN',('CC.EN','REL.BIBLE.OLD','CC.MK'),()),
('VICTOR',('CC.EN','CC.FR','CC.PT','CC.RO'),()),
('DOLORES',('CC.ES','CC.EN'),()),
('SYLVIA',('CC.EN','REG.SCAN','CC.FI','CC.DE'),()),
('GERALDINE','CC.EN',()),
('GLENN',('CC.ST','CC.EN'),()),
('PAULA',('CC.DE','CC.EN','CC.ES','CC.PT','CC.RO','CC.HU','CC.PL','CC.NL','REG.SCAN','CC.HR'),()),
('ALLEN',('CC.EN','CC.ST'),'AL'),
('BRYAN','CC.EN',()),
('EVA',('CC.IT','CC.ES','CC.PT','CC.EN','CC.DE','CC.NL','REG.SCAN','CC.CZ','CC.SI','CC.BG','CC.HR','CC.MK','CC.RU','REL.BIBLE.NEW'),()),
('CRAIG',('CC.ST','CC.EN'),()),
('SHANNON',('CC.IE','CC.EN'),()),
('JAMIE',('CC.ST','CC.EN'),()),
('TRACY','CC.EN',()),
('JUANITA','CC.ES',()),
('LORRAINE','CC.EN',()),
('BEATRICE',('CC.IT','CC.EN'),()),
('BERNICE',('CC.EN','REL.BIBLE.NEW'),()),
('DAWN','CC.EN',()),
('AMBER',('CC.EN','CC.NL'),()),
('CURTIS','CC.EN','CURT'),
('EDWIN',('CC.EN','CC.NL'),'ED'),
('DANIELLE',('CC.FR','CC.EN'),()),
('AUDREY','CC.EN',()),
('TINA',('CC.EN','CC.IT','CC.NL','CC.SI','CC.HR'),()),
('TAYLOR','CC.EN',()),
('CARRIE','CC.EN',()),
('BERTHA',('CC.DE','CC.EN'),()),
('HANNAH',('CC.EN','REL.BIBLE.OLD','CC.FR','CC.DE','CC.NL'),()),
('JUNE','CC.EN',()),
('BERNARD',('CC.EN','CC.FR','CC.PL','CC.HR','CC.SI'),()),
('LEROY','CC.EN',()),
('CRYSTAL','CC.EN',()),
('THEODORE','CC.EN',('TED')),
('JUAN','CC.ES',()),
('AUSTIN','CC.EN',()),
('RAY','CC.',()),
('BRITTANY','CC.EN',()),
('LYNN','CC.EN',()),
('CHRISTIAN',('REL.CHRISTIAN','CC.EN','CC.FR','CC.DE','REG.SCAN'),()),
('TIFFANY','CC.EN',()),
('TODD','CC.EN',()),
('GERTRUDE',('CC.EN','CC.DE','CC.NL'),()),
('JOANNE','CC.EN',()),
('SHEILA',('CC.IE','CC.EN'),()),
('ANITA',('CC.ES','CC.HR','CC.FI','CC.EN'),()),
('SALLY','CC.EN',()),
('GAIL','CC.EN',()),
('RODNEY','CC.EN',()),
('BRADLEY','CC.EN',()),
('CINDY','CC.EN',()),
('ERIN',('CC.EN','CC.IE'),()),
('ELSIE','CC.EN',()),
('VIVIAN',('CC.EN','REG.SCAN'),()),
('ELLA',('CC.EN','REG.SCAN'),()),
('CLIFFORD','CC.EN',()),
('ALEXIS',('CC.DE','CC.FR','CC.EN','CC.GR'),('ALEX')),
('WENDY','CC.EN',()),
('SHERRY','CC.EN',()),
('SUZANNE',('CC.FR','CC.EN'),('SUZY')),
('IDA',('CC.EN','CC.DE','REG..SCAN','CC.NL','CC.IT','CC.ES','CC.PT','CC.HU','CC.SO','CC.HR',),()),
('TRAVIS','CC.EN',()),
('DARLENE','CC.EN',()),
('EILEEN',('CC.IE','CC.EN'),()),
('NATALIE',('CC.FR','CC.EN','CC.DE'),()),

('HUCKLEBERRY','CC.US',''),

)

def build_names():
	cnt = 0
	for name,hint in SurNames:
		#print('name=', name)
		if type(name) != tuple:
			name = (name,)
		if type(hint) != tuple:
			hint = (hint,)
		for n in name:
			n = names.normalize(n)
			for h in hint:
				cnt += 1
				if n in SurnameDict:
					SurnameDict[n].append(h)
				else:
					SurnameDict[n] = [h]
				#print('%s:%s' % (n,h)),
	print('name/hint=',cnt)

GivenNameDict = {}

def build_names():
	cnt = 0
	for name,hints,nicknames in GivenNames:
		if type(name) != tuple:
			name = (name,)
		for n in name:
			n = names.normalize(n)
			if type(hints) != tuple:
				hints = (hints,)
			for h in hints:
				if not hint.is_hint(h):
					print(name,h," is not a hint")
				cnt += 1
				if n in GivenNameDict:
					GivenNameDict[n].append(h)
				else:
					GivenNameDict[n] = [h]
			# unique-ify
			GivenNameDict[n] = list(dict([(x,None) for x in GivenNameDict[n]]).keys())
	print('GivenName name/hint=',cnt)

build_names()

def classify(name):
	norm = names.normalize(name)
	try:
		return GivenNameDict[norm]
	except KeyError:
		return None

if __name__ == '__main__':
	pass

