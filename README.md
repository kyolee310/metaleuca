metaleuca
=========

Metaleuca is a bare-metal provision management system that utilizes open-source software Cobbler via EC2-like CLI API

i.e.

metaleuca-run-instances
metaleuca-describe-instances
metaleuca-terminate-instances
...

Using Metaleuca, a user can select an image(profile) and a set of bare-metal machines(systems), then launch those machines to boot up with the selected image using the command-line tools that feel very much like the EC2 tools, or euca2ools. In other words, instead of launching virtual instances, the user is able to self-provision bare-metal instances, which are managed like EC2 instances.

What are the components of Metaleuca?

Metaleuca Service Layer (Metaleuca SLayer)

Metaleuca Service Layer, a.k.a Metaleuca Slayer, is a lightweight service layer that manages sequencing of operations that handles launching of bare-metal instances, keeping track of status and resources, and terminating instances; all the information is maintained in Metaleuca's own database that is external to Cobbler's database.
Metaleuca2ools

Metaleuca2ools is a set of CLIs that are exposed to users so that they can directly interact with Metaleuca, similar to EC2 tools and euca2ools.

CLI Comparison

Metaleuca  EC2
metaleuca-run-instances	euca-run-instances
metaleuca-describe-instances	euca-describe-instances
metaleuca-terminate-instances	euca-terminate-instances
metalecau-describe-profiles	euca-describe-images

