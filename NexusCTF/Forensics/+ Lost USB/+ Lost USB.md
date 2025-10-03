> [!abstract] Challenge Description
> > Nguyen Vu An Nhan
> ## 150
> Axion Mining Corp's newest hyper-secure, hyper-light feature allows users to set up "zones of control" upon which data can only be accessed from the interface when standing inside them. They promote that outside of them, these files are "virtually the same as deleted by the user". However, there seems to be almost no delay after entering a zone or leaving a zone for the process to occur, some even witness their files "flickering" when close to the border of these zones. We snatched this manager's USB off them but now that we are outside the zone, we can't access it. However, we suspect that there's still a way to access their data. Find out how, and we'll pay you for your trouble.

Trying to mount when I don't know what I'm doing is a pain.

```bash
sudo losetup --find --show usb_work.img
sudo e2fsck -n /dev/loop0
sudo mkdir -p /mnt/usb
sudo mount -o ro /dev/loop0 /mnt/usb
# Found nothing
sudo umount /mnt/usb

photorec usb.img
```
Recovered a few files, flag was hidden in `.png`

---
> [!success] Flag: `NexusCTF{7r4c3s_r3m4in}`
