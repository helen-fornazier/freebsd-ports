--- setup.py.orig	2017-08-29 20:17:21 UTC
+++ setup.py
@@ -30,7 +30,6 @@ setuptools.setup(
     long_description='Google Compute Engine guest environment.',
     name='google-compute-engine',
     packages=setuptools.find_packages(),
-    scripts=glob.glob('scripts/*'),
     url='https://github.com/GoogleCloudPlatform/compute-image-packages',
     version='2.6.0',
     # Entry points create scripts in /usr/bin that call a function.
