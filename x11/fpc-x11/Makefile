# Created by: Alonso Cardenas Marquez <acm@FreeBSD.org>
# $FreeBSD$

CATEGORIES=	x11 lang
PKGNAMESUFFIX=	-x11

COMMENT=	Free Pascal interface to X windows server

USE_FPC=	yes

MASTERDIR=	${.CURDIR}/../../lang/fpc
WRKUNITDIR=	${FPCSRCDIR}/packages/${PKGNAMESUFFIX:S/-//}
EXTRACTUNITDIR=	${WRKUNITDIR}

OPTIONS_DEFINE=	X11
X11_DESC=	Install X libraries
OPTIONS_DEFAULT=	X11

X11_USE=	XORG=xcursor,xfont,xxf86dga,xxf86vm,xi,xinerama,xkbfile,xrandr,xrender,xres,xv

.include "${MASTERDIR}/Makefile"
