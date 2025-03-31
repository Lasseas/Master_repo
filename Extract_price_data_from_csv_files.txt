#extract price data from csv files

import pandas as pd
import os
#######################################################
####code for extracting activation prices############
#######################################################

def extract_and_append_balancing_prices(
    csv_path,
    excel_output_path="NO1_mFRR_Capacity_prices_with_time_2024.xlsx",
    map_code="NO1",
    reserve_type="Manual Frequency Restoration Reserve (mFRR)"
):
    # Load CSV
    df = pd.read_csv(csv_path, sep="\t")
    df.columns = df.columns.str.strip()

    # Filter for area and reserve type
    filtered = df[
        (df["MapCode"] == map_code) &
        (df["ReserveType"] == reserve_type)
    ]

    # Select columns
    selected_columns = ["ISP(UTC)", "UpwardPrice", "DownwardPrice"]
    filtered = filtered[selected_columns]

    # Convert to datetime and remove timezone
    filtered["ISP(UTC)"] = pd.to_datetime(filtered["ISP(UTC)"], utc=True)
    filtered["ISP(UTC)"] = filtered["ISP(UTC)"].dt.tz_localize(None)

    # Extract Month, Day, Hour
    filtered["Month"] = filtered["ISP(UTC)"].dt.month
    filtered["Day"] = filtered["ISP(UTC)"].dt.day
    filtered["Hour"] = filtered["ISP(UTC)"].dt.hour

    # Append to or create Excel file
    if os.path.exists(excel_output_path):
        existing = pd.read_excel(excel_output_path)
        combined = pd.concat([existing, filtered], ignore_index=True)
    else:
        combined = filtered

    combined.to_excel(excel_output_path, index=False)
    print(f"✅ Data from {os.path.basename(csv_path)} added to {excel_output_path}")


# Example usage:


#extract_and_append_balancing_prices(
 #   r"C:\Users\ojviken\OneDrive\Dokumenter\10. semester\Til master\Data til priser\Historisk markeds og soldata 2022-2024\Prices forActivation\2024_02_PricesOfActivatedBalancingEnergy_17.1.F_r3.csv"
#)



#######################################################
####code for extracting capacity prices prices############
#######################################################

import pandas as pd
import os



def extract_and_append_capacity_prices(
    csv_path,
    output_excel_path="NO1_mFRR_Capacity_Prices_UpDown.xlsx",
    map_code="NO1",
    reserve_type="Manual Frequency Restoration Reserve (mFRR)"
):
    # Load CSV (tab-separated)
    df = pd.read_csv(csv_path, sep="\t", low_memory=False)
    df.columns = df.columns.str.strip()

    # Filter for NO1, mFRR (include all prices: positive, negative, zero)
    df_filtered = df[
        (df["MapCode"] == map_code) &
        (df["ReserveType"] == reserve_type) &
        (df["Direction"].isin(["Up", "Down"])) &
        (df["TimeHorizon"].isin(["Daily", "Hourly"]))
    ].copy()

    # Convert time and extract parts
    df_filtered["ISP(UTC)"] = pd.to_datetime(df_filtered["ISP(UTC)"], utc=True)
    df_filtered["ISP(UTC)"] = df_filtered["ISP(UTC)"].dt.tz_localize(None)
    df_filtered["Month"] = df_filtered["ISP(UTC)"].dt.month
    df_filtered["Day"] = df_filtered["ISP(UTC)"].dt.day
    df_filtered["Hour"] = df_filtered["ISP(UTC)"].dt.hour

    # Pivot Up and Down directions into separate columns
    df_pivot = df_filtered.pivot_table(
        index=["ISP(UTC)", "Month", "Day", "Hour"],
        columns="Direction",
        values="Price(MW/ISP)",
        aggfunc="first"
    ).reset_index()

    df_pivot.columns.name = None
    df_pivot.rename(columns={
        "Up": "CapacityPrice_Up",
        "Down": "CapacityPrice_Down"
    }, inplace=True)

    # Append to or create Excel file
    if os.path.exists(output_excel_path):
        existing = pd.read_excel(output_excel_path)
        combined = pd.concat([existing, df_pivot], ignore_index=True)
        combined.drop_duplicates(subset=["ISP(UTC)", "Hour"], inplace=True)
    else:
        combined = df_pivot

    combined.to_excel(output_excel_path, index=False)
    print(f"✅ Data from {os.path.basename(csv_path)} added to: {output_excel_path}")


#extract_and_append_capacity_prices(
#    r"C:\Users\ojviken\OneDrive\Dokumenter\10. semester\Til master\Data til priser\Historisk markeds og soldata 2022-2024\Prices for Balancing Reserves\2025_01_AmountAndPricesPaidOfBalancingReservesUnderContract_17.1.B_C_r2.csv"
#)
