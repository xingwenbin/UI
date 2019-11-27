from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://sahitest.com/demo/selectTest.htm')
# driver.execute_script()
driver.get_att

s1 = Select(driver.find_element_by_id('s1Id'))  # 实例化Select
print(s1)

s1.select_by_index(1)  # 选择第二项选项：o1
s1.select_by_value("o2")  # 选择value="o2"的项
s1.select_by_visible_text("o3")  # 选择text="o3"的值，即在下拉时我们可以看到的文本

driver.quit()

