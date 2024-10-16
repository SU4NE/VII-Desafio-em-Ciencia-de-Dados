import pickle
import pandas as pd
from typing import Tuple


modelo_caminho = './models/CatBoost.pkl'
modelo_scaler = './scaler.pkl'

with open(modelo_caminho, 'rb') as arquivo:
    model = pickle.load(arquivo)

with open(modelo_scaler, "rb") as f:
    scaler = pickle.load(f)

def preprocess_data(solar_wind: pd.DataFrame, sunspots: pd.DataFrame) -> pd.DataFrame:
    """
    Pré-processa os dados de vento solar e manchas solares.

    Parameters
    ----------
    solar_wind : pd.DataFrame
        Dados de vento solar.
    sunspots : pd.DataFrame
        Dados de manchas solares.

    Returns
    -------
    pd.DataFrame
        Dados pré-processados e normalizados.
    """
    sw_data = solar_wind.copy()
    ssn_data = sunspots.copy()
    
    sw_data["timedelta"] = pd.to_timedelta(sw_data["timedelta"])
    sw_data.drop(columns=["source"], inplace=True)
    sw_data.set_index(["period", "timedelta"], inplace=True)

    ssn_data["timedelta"] = pd.to_timedelta(ssn_data["timedelta"])
    ssn_data.set_index(["period", "timedelta"], inplace=True)

    sw_data = sw_data.join(ssn_data)
    sw_data["smoothed_ssn"] = sw_data["smoothed_ssn"].ffill()
    sw_data = sw_data.apply(lambda col: col.interpolate().ffill().bfill(), axis=0)
    
    def remove_outliers_iqr(df, tx=1.2):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - tx * IQR
        upper_bound = Q3 + tx * IQR
        return df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]

    sw_data = remove_outliers_iqr(sw_data)
    
    df_normalized = pd.DataFrame(scaler.transform(sw_data), columns=sw_data.columns, index=sw_data.index)
    
    return df_normalized

def predict_dst(
    solar_wind: pd.DataFrame,
    sunspots: pd.DataFrame
) -> Tuple[float, float, float]:
    """
    Realiza a predição para os tempos t, t+1, e t+2 horas.

    Parameters
    ----------
    solar_wind : pd.DataFrame
        Últimos dados de vento solar.
    sunspots : pd.DataFrame
        Dados recentes de manchas solares.

    Returns
    -------
    Tuple[float, float, float]
        Predições para t, t+1, e t+2 horas.
    """
    model_input = preprocess_data(solar_wind, sunspots)
    t0, t1, t2 = model.predict(model_input)[0]

    return t0, t1, t2
