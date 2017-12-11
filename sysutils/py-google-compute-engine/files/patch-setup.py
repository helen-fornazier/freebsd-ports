--- setup.py.orig	2017-11-29 19:23:20 UTC
+++ setup.py
@@ -30,7 +30,6 @@ setuptools.setup(
     long_description='Google Compute Engine guest environment.',
     name='google-compute-engine',
     packages=setuptools.find_packages(),
-    scripts=glob.glob('scripts/*'),
     url='https://github.com/GoogleCloudPlatform/compute-image-packages',
     version='2.7.2',
     # Entry points create scripts in /usr/bin that call a function.
