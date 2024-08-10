from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import requests

class ExchangeRateView(APIView):
    def get(self, request, *args, **kwargs):
        url = "https://www.bcv.org.ve/"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except RequestException as e:
            return Response({"error": f"Failed to retrieve data from BCV website: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            try:
                dolar_div = soup.find("div", {"id": "dolar"})
                if not dolar_div:
                    raise ValueError("USD rate div not found")
                usd_rate_element = dolar_div.find("strong")
                if not usd_rate_element:
                    raise ValueError("USD rate element not found")
                usd_rate_text = usd_rate_element.text.strip()
                usd_rate = round(float(usd_rate_text.replace(',', '.')), 2)

                date_span = soup.find("span", {"class": "date-display-single"})
                if not date_span:
                    raise ValueError("Date span not found")
                date_value = date_span.text.strip()
                date_value_cleaned = " ".join(date_value.split())

                month_mapping = {
                    'Enero': '01', 'Febrero': '02', 'Marzo': '03', 'Abril': '04',
                    'Mayo': '05', 'Junio': '06', 'Julio': '07', 'Agosto': '08',
                    'Septiembre': '09', 'Octubre': '10', 'Noviembre': '11', 'Diciembre': '12'
                }

                parts = date_value_cleaned.split()
                day = parts[1].strip(',')
                month = month_mapping.get(parts[2], '01')
                year = parts[3]
                date_formatted = f"{year}-{month}-{day}"

                data = {
                    "usd_rate": usd_rate,
                    "date_value": date_formatted
                }
                return Response(data, status=status.HTTP_200_OK)
            except (AttributeError, ValueError) as e:
                return Response({"error": f"Could not extract exchange rate or date: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Failed to retrieve data from BCV website"}, status=status.HTTP_400_BAD_REQUEST)
