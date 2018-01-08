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
RUN_DEPENDS=	gsed:textproc/gsed \
		${LOCALBASE}/lib/pam_mkhomedir.so:security/pam_mkhomedir

USE_GITHUB=	yes
GH_ACCOUNT=	GoogleCloudPlatform
GH_PROJECT=	compute-image-packages
GH_TAGNAME=	20171213

USES=		gmake
USE_LDCONFIG=	yes
USE_GCC=	any
MAKE_ARGS=	JSON_INCLUDE_PATH=${LOCALBASE}/include/json-c \
		BIN_INSTALL_PATH=/bin \
		PAM_INSTALL_PATH=/lib \
		AUTHKEYS_INSTALL_PATH=/bin \
		NSS_LIBRARY_SONAME=nss_oslogin.so.1

WRKSRC_SUBDIR=	google_compute_engine_oslogin

SHEBANG_FILES=	bin/google_oslogin_control

post-patch:
		@${REINPLACE_CMD} -e 's|/etc/sudoers.d|${PREFIX}/etc/sudoers.d|g' ${WRKSRC}/bin/google_oslogin_control
		@${REINPLACE_CMD} -e 's|/usr/bin|${PREFIX}/bin|g' ${WRKSRC}/bin/google_oslogin_control

post-install:
		ln -sf libnss_${PORTNAME}-${PORTVERSION}.so ${STAGEDIR}${PREFIX}/lib/nss_oslogin.so.1

.include <bsd.port.mk>
