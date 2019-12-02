from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

fo = open("D:\\work\\done.txt", 'r')
reg_list = fo.readlines()
fo.close()

fo = open("D:\\work\\done.txt", 'a')
f_non_reg = open("D:\\work\\on_regestered_pages.txt", 'a+')

file_name = "D:\\work\\products List2.csv"
f = open(file_name, 'a')
header = "Product Name, Price, Viewed, Sold, Link, No. in stock \n"
f.write(header)

non_regestered_pages = list()
links_list = list()

for link in reg_list:
	link = link.strip()
	links_list.append(link)

pages = [
	"https://uge-one.com/3d-printer-cnc-parts.html",
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-kits.html",
	"https://uge-one.com/3d-printer-cnc-parts/aluminium-slot-profile-rails-and-accessories.html",
	"https://uge-one.com/3d-printer-cnc-parts/bolts-nuts.html",
	"https://uge-one.com/3d-printer-cnc-parts/filament-pla-abs.html",
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-accessories-egypt.html",
	"https://uge-one.com/3d-printer-cnc-parts/cnc-mechanics-electronics.html",
	"https://uge-one.com/arduino/arduino-boards.html",
	"https://uge-one.com/arduino/arduino-shield.html",
	"https://uge-one.com/arduino/modules-accessory-boards.html",
	"https://uge-one.com/embedded-boards.html",
	"https://uge-one.com/embedded-boards/arm.html",
	"https://uge-one.com/embedded-boards/fpga-boards-accessories.html",
	"https://uge-one.com/embedded-boards/microcontroller-kits.html",
	"https://uge-one.com/embedded-boards/modules-accessory-boards.html",
	"https://uge-one.com/embedded-boards/raspberry-pi.html",
	"https://uge-one.com/embedded-boards/wireless-modules.html",
	"https://uge-one.com/components/7-segments-display-led-s.html",
	"https://uge-one.com/components/ndfeb-neodymium-magnet.html",
	"https://uge-one.com/components/solar-cell-pv-and-led-solar-street-light.html",
	"https://uge-one.com/components/special-request-items.html",
	"https://uge-one.com/components/triac-diac-thyristors.html",
	"https://uge-one.com/components/batteries-chargers.html",
	"https://uge-one.com/components/integrated-circuits-ics.html",
	"https://uge-one.com/components/boxes-enclosure.html",
	"https://uge-one.com/components/bread-boards-accessories.html",
	"https://uge-one.com/components/bridge-rectifiers.html",
	"https://uge-one.com/components/buzzers-speakers.html",
	"https://uge-one.com/components/capacitors.html",
	"https://uge-one.com/components/coils.html",
	"https://uge-one.com/components/connectors.html",
	"https://uge-one.com/components/sensors.html",
	"https://uge-one.com/components/crystal-oscillators.html",
	"https://uge-one.com/components/dc-to-dc-converters.html",
	"https://uge-one.com/components/diodes-zener-diodes.html",
	"https://uge-one.com/components/fans-heatsinks.html",
	"https://uge-one.com/components/fuses-and-holders.html",
	"https://uge-one.com/components/resistors.html",
	"https://uge-one.com/components/ic-sockets.html",
	"https://uge-one.com/components/key-pads.html",
	"https://uge-one.com/components/relays.html",
	"https://uge-one.com/components/switches.html",
	"https://uge-one.com/components/transistors.html",
	"https://uge-one.com/components/voltage-regulator.html",
	"https://uge-one.com/test-equipment.html",
	"https://uge-one.com/test-equipment/accessories-of-test-equipments.html",
	"https://uge-one.com/test-equipment/anemometer.html",
	"https://uge-one.com/test-equipment/calibrators.html",
	"https://uge-one.com/test-equipment/clamp-meter.html",
	"https://uge-one.com/test-equipment/dc-electronic-load.html",
	"https://uge-one.com/test-equipment/distance-meter.html",
	"https://uge-one.com/test-equipment/earth-resistance-tester.html",
	"https://uge-one.com/test-equipment/electrical-tool.html",
	"https://uge-one.com/test-equipment/flow-meter.html",
	"https://uge-one.com/test-equipment/gas-detector.html",
	"https://uge-one.com/test-equipment/gauss-and-tesla-meter.html",
	"https://uge-one.com/test-equipment/humidity.html",
	"https://uge-one.com/test-equipment/insulation-resistance-tester-megger.html",
	"https://uge-one.com/test-equipment/laboratory.html",
	"https://uge-one.com/test-equipment/lcr-l-c-r-z-d-q-esr-theta-meter.html",
	"https://uge-one.com/test-equipment/light-meter.html",
	"https://uge-one.com/test-equipment/logic-analyzer.html",
	"https://uge-one.com/test-equipment/maintenance-tools.html",
	"https://uge-one.com/test-equipment/micro-ohm-meter.html",
	"https://uge-one.com/test-equipment/milli-ohm-meter.html",
	"https://uge-one.com/test-equipment/multimeters.html",
	"https://uge-one.com/test-equipment/oscilloscope.html",
	"https://uge-one.com/test-equipment/oxygen-meter-o2.html",
	"https://uge-one.com/test-equipment/ph-meter.html",
	"https://uge-one.com/test-equipment/power-analyzer.html",
	"https://uge-one.com/test-equipment/power-meter.html",
	"https://uge-one.com/test-equipment/power-supply.html",
	"https://uge-one.com/test-equipment/rcd-testers.html",
	"https://uge-one.com/test-equipment/solar-cell.html",
	"https://uge-one.com/test-equipment/sound-and-noise-meter.html",
	"https://uge-one.com/test-equipment/spectrum-analyzer.html",
	"https://uge-one.com/test-equipment/tachometer.html",
	"https://uge-one.com/test-equipment/temperature.html",
	"https://uge-one.com/test-equipment/variac-(ac-regulator-transformer).html",
	"https://uge-one.com/test-equipment/uni-t.html",
	"https://uge-one.com/bread-boards-accessories.html",
	"https://uge-one.com/tools.html",
	"https://uge-one.com/tools/cable-cutter-strippers.html",
	"https://uge-one.com/tools/loupes-and-magnifiers.html",
	"https://uge-one.com/tools/pliers.html",
	"https://uge-one.com/tools/screw-drivers.html",
	"https://uge-one.com/tools/soldering-accessories.html",
	"https://uge-one.com/tools/tools-case.html",
	"https://uge-one.com/tools/tweezers.html",
	"https://uge-one.com/robotics-motors/brushless-motors.html",
	"https://uge-one.com/robotics-motors/dc-motors.html",
	"https://uge-one.com/robotics-motors/robot-kits.html",
	"https://uge-one.com/robotics-motors/rotary-encoders.html",
	"https://uge-one.com/robotics-motors/servo-motors.html",
	"https://uge-one.com/robotics-motors/stepper-motors.html",
	"https://uge-one.com/robotics-motors/wheels-accessories.html",
	"https://uge-one.com/robotics-motors/robot-controller.html",
	"https://uge-one.com/robotics-motors/motor-drivers.html",
	"https://uge-one.com/batteries-chargers.html",
	"https://uge-one.com/batteries-chargers/battery.html",
	"https://uge-one.com/batteries-chargers/battery-holders.html",
	"https://uge-one.com/integrated-circuits-ics/ad-da.html",
	"https://uge-one.com/integrated-circuits-ics/can-module.html",
	"https://uge-one.com/integrated-circuits-ics/digital-potentiometer-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/dtmf-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/igbt-mosfet-driver-ic.html",
	"https://uge-one.com/integrated-circuits-ics/instrumentation-amplifiers.html",
	"https://uge-one.com/integrated-circuits-ics/led-drivers-ic.html",
	"https://uge-one.com/integrated-circuits-ics/memory-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/microcontrollers.html",
	"https://uge-one.com/integrated-circuits-ics/microprocessor-chips.html",
	"https://uge-one.com/integrated-circuits-ics/motor-drivers.html",
	"https://uge-one.com/integrated-circuits-ics/motor-drivers-controllers.html",
	"https://uge-one.com/integrated-circuits-ics/npn-transistor-array-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/op-amp.html",
	"https://uge-one.com/integrated-circuits-ics/optocouplers.html",
	"https://uge-one.com/integrated-circuits-ics/pulse-width-modulator.html",
	"https://uge-one.com/integrated-circuits-ics/real-time-clock-(rtc).html",
	"https://uge-one.com/integrated-circuits-ics/sensing-measuring-ic.html",
	"https://uge-one.com/integrated-circuits-ics/spacial-function-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/timers-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/ttl-cmos-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/ttl-cmos-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/voltage-references.html",
	"https://uge-one.com/integrated-circuits-ics/amplifiers-ic-s.html",
	"https://uge-one.com/integrated-circuits-ics/comparators.html",
	"https://uge-one.com/switches.html",
	"https://uge-one.com/switches/dip-switchs.html",
	"https://uge-one.com/switches/micro-limit-switchs.html",
	"https://uge-one.com/switches/pcb-mount-switches.html",
	"https://uge-one.com/switches/power-rocker-switches.html",
	"https://uge-one.com/switches/reed-magnetic-switches.html",
	"https://uge-one.com/switches/tact-press-switches.html",
	"https://uge-one.com/switches/toggle-switches.html",	
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-accessories-egypt/3d-printer-electronics.html",
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-accessories-egypt/3d-printer-extruder-accessories.html",
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-accessories-egypt/3d-printer-filament.html",
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-accessories-egypt/3d-printer-general-accessories.html",
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-accessories-egypt/3d-printer-motion-bearing.html",
	"https://uge-one.com/3d-printer-cnc-parts/3d-printer-accessories-egypt/3d-printer-wiring.html",
]

for page_url in pages:
	for i in range(1,22):
		my_url = page_url + "?page=" + str(i)
		print(my_url)
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()

		page_soup = soup(page_html, "html.parser")
		page_soup = page_soup.findAll("div" , {"class":"name"})

		print(len(page_soup))
		if len(page_soup) < 13 :
			break

		for container in page_soup:
			container_url = container.a["href"]
			if container_url in links_list:
				print(container_url + " is in the list")
				continue
			if container_url is "https://uge-one.com/apc-by-schneider-electric.html":
				links_list.append(container_url)
				continue
			links_list.append(container_url)

			try:
				uClient = uReq(container_url)
				product_html = uClient.read()
				uClient.close()
			except Exception as e:
				f_non_reg.write(str(container_url.encode('utf-8')))
				continue
				raise e
			

			page_soup = soup(product_html, "html.parser")

			if len(page_soup.findAll("div", {"class" : "product-left"})):
				print(container_url)
				try:
					price = page_soup.find("div", {"class": "product-price"}).text
					
				except Exception as e:
					price = "Error"

				if price is "Error":
					try:
						price = page_soup.find("div", {"class": "product-price-new"}).text
					except Exception as e:
						price = "Error"
					
				try:
					in_stock = page_soup.find("li", {"class" : "product-stock in-stock"}).text[13:]
				except Exception as e:
					in_stock = 'Out of Stock'

				sold = page_soup.find("div", {"class": "product-sold"}).b.text[15:]
				views = page_soup.find("div", {"class": "product-views"}).b.text[15:]

				f.write(container.text.replace(',', '|') + ',' + price.replace(',','') + ',' + views + ',' + sold + ',' + container_url + ',' + in_stock + '\n')
				fo.write(container_url + '\n')
			else:
				pages.append(container_url)
				f_non_reg.write(container_url + '\n')

f_non_reg.close()
fo.close()
f.close()