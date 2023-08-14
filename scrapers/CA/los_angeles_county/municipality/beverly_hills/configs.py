webpage = "http://www.beverlyhills.org/departments/policedepartment/crimeinformation/crimestatistics/web.jsp"
'''
Click the links that lead to the files, and copy their paths. **NOTE:** Ensure that files all match paths, otherwise remove a level until they match
Also ensure that domain stays the same
Verify on page that the href to the file contains the domain, if it doesn't, uncomment domain
'''
web_path = "/cbhfiles/storage/files/"
domain = "http://www.beverlyhills.org"
sleep_time = 5   # Set to desired sleep time
domain_included = False
