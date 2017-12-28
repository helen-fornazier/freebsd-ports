# $FreeBSD$

PORTNAME=	google-compute-engine-oslogin
PORTVERSION=	1.1.2
CATEGORIES=	sysutils
MASTER_SITES=	GH

MAINTAINER=	helen.koike@collabora.com
COMMENT=	OS Login Guest Environment for Google Compute Engine

LICENSE=	APACHE20
LICENSE_FILE=	${WRKSRC}/../LICENSE

LIB_DEPENDS=	libcurl.so:ftp/curl \
		libjson-c.so:devel/json-c

USE_GITHUB=	yes
GH_ACCOUNT=	GoogleCloudPlatform
GH_PROJECT=	compute-image-packages
GH_TAGNAME=	20171213

USES=		gmake shebangfix
MAKE_ARGS=	JSON_INCLUDE_PATH=${LOCALBASE}/include/json-c \
		NSS_INSTALL_PATH=${LOCALBASE}/lib \
		PAM_INSTALL_PATH=${LOCALBASE}/lib/security \
		AUTHKEYS_INSTALL_PATH=${LOCALBASE}/bin

USE_GCC=	yes

WRKSRC_SUBDIR=	google_compute_engine_oslogin

SHEBANG_FILES=	bin/google_oslogin_control

.include <bsd.port.mk>
