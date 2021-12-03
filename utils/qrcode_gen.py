# simple malicious qrcode generator in python
import qrcode
import click

try:

	@click.command()
	@click.option('--payload', '-p', type=str, help='generate qrcode using single payload or using malicious url')
	@click.option('--name', '-n', type=str, help='the name of generated qrcode ')
	def qrcode_gen(payload, name):
		qr = qrcode.QRCode(version=3, box_size=15,border=5)

		data = payload

		qr.add_data(data)
		qr.make(fit=False)

		img = qr.make_image(fill='black', back_color='white')
		img.save(name)
		print('[*] qrcode generated ! ')
	if __name__ == "__main__":
		qrcode_gen()

except AttributeError:
	print('[*] try python3 qrcode_gen.py --help')