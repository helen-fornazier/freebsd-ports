# Created by: Philip M. Gollucci <philip@p6m7g8.com>
# $FreeBSD$

PORTNAME=	DBIx-Tree
PORTVERSION=	1.97
CATEGORIES=	databases perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Perl module for generating a tree from a self-referential table

LICENSE=	ART20

BUILD_DEPENDS=	p5-DBI>=1.622:databases/p5-DBI
RUN_DEPENDS:=	${BUILD_DEPENDS}
TEST_DEPENDS=	p5-DBD-SQLite>=1.37:databases/p5-DBD-SQLite

USES=		perl5 tar:tgz
USE_PERL5=	configure

.include <bsd.port.mk>
