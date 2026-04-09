import requests
import pandas as pd

BASE = "https://consultaelectoral.onpe.gob.pe"

def consultar_dni(dni, token):
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    })

    r1 = s.post(f"{BASE}/v1/api/busqueda/dni", json={
        "numeroDocumento": str(dni),
        "recaptcha": token
    })

    if r1.status_code != 200:
        return None

    data = r1.json().get("data", {})
    jwt = data.get("token")
    if not jwt:
        return None

    s.headers["Authorization"] = f"Bearer {jwt}"
    r2 = s.post(f"{BASE}/v1/api/consulta/definitiva", json={})

    if r2.status_code == 200:
        return r2.json().get("data")

    return None


def main():
    token = input("Token: ").strip()
    df = pd.read_excel("dnis.xlsx")

    resultados = []

    for dni in df["dni"]:
        data = consultar_dni(dni, token)

        if data:
            resultados.append({
                "DNI": dni,
                "Nombres": data.get("nombres"),
                "Apellidos": data.get("apellidos"),
                "Miembro": "SÍ" if data.get("miembroMesa") else "NO"
            })
        else:
            resultados.append({
                "DNI": dni,
                "Nombres": "Error",
                "Apellidos": "",
                "Miembro": ""
            })

    pd.DataFrame(resultados).to_excel("resultado.xlsx", index=False)


if __name__ == "__main__":
    main()