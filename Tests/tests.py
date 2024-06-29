import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_path_1 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\cert.cer"
file_path_2 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\Таксер Тест Тестович.cer"
file_path_3 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\Нестеренко_Володимир_Борисович_(Тест)-8101916.cer"
file_path_4 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\Сухаренко_Олег_Андрiйович_(Тест)-8101900.cer"
file_path_5 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\idd_2019.cer"
file_path_6 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\privat_2018.cer"
file_path_7 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\cert2.cer"
file_path_8 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\czo_2017.cer"
file_path_9 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\ekpp_sign_2014.cer"
file_path_10 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\Тестувальник Tellipse 1111.cer"
file_path_11 = r"C:\Users\Valentyn\Downloads\Сертифікати\test_certs\test_certs\Тестовий_платник_4_(Тест)-8101906.cer"

driver = webdriver.Chrome()
driver.maximize_window()

def test_adding_first_certificate():
    driver.get("https://js-55fbfg.stackblitz.io/")

    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Run this project']")))
    button.click()

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_1)

    time.sleep(5)

def test_checking_datail_of_certificate():
    user_name = 'Таксер Тест Тестерович'
    subject = 'UA-22723472'
    valid_from = '2015-04-08'
    valid_till = '2017-04-08'

    user_name_certificate = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//*[@class='ng-binding'])[1]")))
    user_subject_certificate = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//td[@class='ng-binding'])[2]")))
    user_valid_from = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//td[@class='ng-binding'])[3]")))
    user_valid_till = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//td[@class='ng-binding'])[4]")))


    if user_name == user_name_certificate.text:
        print("Ім'я в сертифікаті і на WEB однакове")
    else:
        print(f"Ім'я не співпадає: {user_name} != {user_name_certificate.text}")

    if subject == user_subject_certificate.text:
        print("Суб'єкт в сертифікаті і на WEB однаковий")
    else:
        print(f"Суб'єкт не співпадає: {subject} != {user_subject_certificate.text}")

    if valid_from == user_valid_from.text:
        print("Дата початку дії сертифікату в сертифікаті і на WEB однакові")
    else:
        print(f"Дата початку дії не співпадає: {valid_from} != {user_valid_from.text}")

    if valid_till == user_valid_till.text:
        print("Дата закінчення дії сертифікату в сертифікаті і на WEB однакові")
    else:
        print(f"Дата закінчення дії не співпадає: {valid_till} != {user_valid_till.text}")



def test_add_second_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_3)


def test_add_fourth_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_4)


def test_add_fifth_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_5)


def test_add_sixth_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_6)


def test_add_seventh_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_7)


def test_add_eighth_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_8)


def test_add_ninth_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_9)


def test_add_tenth_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_10)


def test_add_eleventh_certificate():

    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
    add_button.click()

    dropbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//dropbox[@class='dropbox ng-isolate-scope']")))

    driver.execute_script("""
        var dropbox = arguments[0];
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';
        input.onchange = function() {
            var rect = dropbox.getBoundingClientRect();
            var dataTransfer = new DataTransfer();
            dataTransfer.items.add(input.files[0]);
            var event = new DragEvent('drop', {
                dataTransfer: dataTransfer,
                bubbles: true,
                cancelable: true,
                composed: true,
                clientX: rect.left + (rect.width / 2),
                clientY: rect.top + (rect.height / 2)
            });
            dropbox.dispatchEvent(event);
        };
        document.body.appendChild(input);
        return input;
    """, dropbox).send_keys(file_path_11)

    time.sleep(10)
    driver.quit()

