import csv
import unittest


def url_gen(input):
    arr = input.split("_")
    tproduct_code = arr[1].split("-")
    s1 = tproduct_code[2]
    finalProductCode = tproduct_code[0] + "-" + tproduct_code[1] + "-" + ''.join([i for i in s1 if not i.isdigit()])
    date = arr[3]
    year = date[1:5]
    day_of_year = date[5:8]
    hour = date[8:10]
    fs = "https://noaa-goes18.s3.amazonaws.com/{}/{}/{}/{}/{}".format(finalProductCode, year, day_of_year, hour, input)
    return fs


class TestUrlGen(unittest.TestCase):
    def test_url_gen(self):
        with open('test_cases.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                input = row[0]
                expected_output = row[1]
                output = url_gen(input)
                self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
