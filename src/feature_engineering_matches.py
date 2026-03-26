import pandas as pd
import numpy as np
import os

def run_feature_engineering():
    # 1. Cargar el dataset de partidos
    data_path = '/home/julianxd/code/machine/Prediccion-Futbolistica/data/matches.csv'
    if not os.path.exists(data_path):
        print(f"Error: No se encontró {data_path}")
        return

    df_matches = pd.read_csv(data_path)
    df_matches['date'] = pd.to_datetime(df_matches['date'], format='%d/%m/%Y')
    df_matches = df_matches.sort_values(by='date')

    def get_rolling_stats(df, rolling_window=5):
        """Calcula promedios móviles para cada equipo"""
        team_matches = []
        all_teams = pd.concat([df['home_team'], df['away_team']]).unique()
        
        for team in all_teams:
            # Partidos donde el equipo fue local
            home_side = df[df['home_team'] == team].copy()
            home_side['team'] = team
            home_side['is_home'] = 1
            home_side['goals_for'] = home_side['fthg']
            home_side['goals_against'] = home_side['ftag']
            home_side['shots_for'] = home_side['hs']
            home_side['shots_on_target'] = home_side['hst']
            
            # Partidos donde el equipo fue visitante
            away_side = df[df['away_team'] == team].copy()
            away_side['team'] = team
            away_side['is_home'] = 0
            away_side['goals_for'] = away_side['ftag']
            away_side['goals_against'] = away_side['fthg']
            away_side['shots_for'] = away_side['as_']
            away_side['shots_on_target'] = away_side['ast']
            
            team_df = pd.concat([home_side, away_side]).sort_values('date')
            
            # Calculamos el promedio móvil (con shift para no incluir el partido actual)
            cols_to_roll = ['goals_for', 'goals_against', 'shots_for', 'shots_on_target']
            for col in cols_to_roll:
                team_df[f'rolling_{col}'] = team_df[col].shift(1).rolling(window=rolling_window).mean()
            
            team_matches.append(team_df[['id', 'team', 'rolling_goals_for', 'rolling_goals_against', 'rolling_shots_for', 'rolling_shots_on_target']])

        # Unir todo de vuelta al dataframe principal
        rolling_all = pd.concat(team_matches)
        
        # Unir para Home
        df = df.merge(rolling_all, left_on=['id', 'home_team'], right_on=['id', 'team'], how='left')
        df.rename(columns={
            'rolling_goals_for': 'rolling_goals_scored_h',
            'rolling_goals_against': 'rolling_goals_conceded_h',
            'rolling_shots_for': 'rolling_shots_h',
            'rolling_shots_on_target': 'rolling_shots_ot_h'
        }, inplace=True)
        # Drop redundant merge columns
        df.drop(columns=['team'], inplace=True)
        
        # Unir para Away
        df = df.merge(rolling_all, left_on=['id', 'away_team'], right_on=['id', 'team'], how='left', suffixes=('', '_a'))
        df.rename(columns={
            'rolling_goals_for': 'rolling_goals_scored_a',
            'rolling_goals_against': 'rolling_goals_conceded_a',
            'rolling_shots_for': 'rolling_shots_a',
            'rolling_shots_on_target': 'rolling_shots_ot_a'
        }, inplace=True)
        df.drop(columns=['team'], inplace=True)
        
        return df

    # Ejecutar y Guardar
    df_processed = get_rolling_stats(df_matches)
    # Seleccionar solo las columnas necesarias para el modelo + metadatos
    cols_to_keep = ['id', 'date', 'home_team', 'away_team', 'ftr', 'b365h', 'b365d', 'b365a', 
                    'rolling_goals_scored_h', 'rolling_goals_conceded_h', 'rolling_shots_h', 'rolling_shots_ot_h',
                    'rolling_goals_scored_a', 'rolling_goals_conceded_a', 'rolling_shots_a', 'rolling_shots_ot_a']
    
    df_processed = df_processed[cols_to_keep]
    df_processed.dropna(inplace=True) 
    
    out_path = '/home/julianxd/code/machine/Prediccion-Futbolistica/data/matches_processed.csv'
    df_processed.to_csv(out_path, index=False)
    print(f"Dataset procesado con {df_processed.shape[0]} partidos y nuevas estadísticas.")

if __name__ == "__main__":
    run_feature_engineering()
