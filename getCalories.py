from flask import Flask, redirect, url_for
import sqlite3
import database
import userStore

def get_met(activity, intensity):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor
    cur = conn.cursor()

    # Get MET
    try:
        res = cur.execute("SELECT met FROM metTable WHERE activity = ? and intensity = ?", (activity,intensity))
        result = res.fetchone()
        if result != None:
            met = result[0]
        else:
            print(f"No met found for {activity} {intensity}")
            return 0
    except sqlite3.Error as e:
        print(f"Database error: {e}")  # Prints the full error message
        print(f"No met found for {activity} {intensity}")
        result = None
        cur.close()
        conn.close()
        return 0
    
    cur.close()
    conn.close()
    return met  

def get_calories(activity, intensity, minutes):    
    userName = userStore.get_user()
    weight = userStore.get_weight()

    if weight == 0:
        message = "No weight recorded"
        print(message)
        return -1

    global kgWeight
    kgWeight = weight * 2.2
    met = get_met(activity, intensity)
    cals =round(met * 3.5 * kgWeight/200 * int(minutes), 2)

    return cals