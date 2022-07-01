from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time

# A function that takes a Google Image search link and gets the Image URLS for a set ammount of pictures
# Returns a list of URLS
def get_images_from_google(wd, delay, max_images, url):
	def scroll_to_end(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)
	
	wd.get(url)

	image_urls = set()
	actual_index = 0
	max_index = 1

	while actual_index <= max_images:

		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")
		if actual_index + 5 >= max_index:
			scroll_to_end(wd)

		for img in thumbnails[actual_index:max_images+1]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue
			

			images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				actual_index += 1
				if image.get_attribute('src') in image_urls:
					max_images +=1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")

	return image_urls

# A function that takes a list of URLS and Downloads the images to the local computer
def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)
