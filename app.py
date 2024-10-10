from flask import Flask, request, jsonify
from dbconfig1 import dbconfig
from datetime import datetime

app = Flask(__name__)

# Activate SIM Card
@app.route('/activate', methods=['POST'])
def activate_sim():
    data = request.json
    sim_number = data.get('sim_number')

    # Check for missing or invalid input
    if not sim_number:
        return jsonify({"error": "SIM number is required"}), 400
    
    try:
        db = dbconfig()
        cursor = db.cursor()

        # Check if the SIM card exists
        cursor.execute('SELECT status FROM sim_card.info WHERE sim_number = %s;', (sim_number,))
        result = cursor.fetchone()

        if result is None:
            return jsonify({"error": "SIM card not found"}), 404

        current_status = result[2]

        # Check if the SIM card is already active
        if current_status == 'active':
            return jsonify({"error": f"SIM card {sim_number} is already active."}), 400

        # Update the SIM card status and set the activation date
        cursor.execute('''UPDATE sim_card.info SET status = %s, activation_date = %s WHERE sim_number = %s;''',
                       ('active', datetime.now(), sim_number))

        db.commit()
        return jsonify({"message": f"SIM card {sim_number} activated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        db.close()

# Deactivate SIM Card
@app.route('/deactivate', methods=['POST'])
def deactivate_sim():
    data = request.json
    sim_number = data.get('sim_number')

    # Check for missing or invalid input
    if not sim_number:
        return jsonify({"error": "SIM number is required"}), 400

    try:
        db = dbconfig()
        cursor = db.cursor()

        # Check if the SIM card exists
        cursor.execute('SELECT status FROM sim_card.info WHERE sim_number = %s;', (sim_number,))
        result = cursor.fetchone()

        if result is None:
            return jsonify({"error": "SIM card not found"}), 404

        current_status = result[0]

        # Check if the SIM card is already inactive
        if current_status == 'inactive':
            return jsonify({"error": f"SIM card {sim_number} is already inactive."}), 400

        # Update the SIM card status to inactive
        cursor.execute('''UPDATE sim_card.info SET status = %s, activation_date = NULL WHERE sim_number = %s;''',
                       ('inactive', sim_number))

        db.commit()
        return jsonify({"message": f"SIM card {sim_number} deactivated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        db.close()

# Get SIM Details
@app.route('/sim-details/<sim_number>', methods=['GET'])
def get_sim_details(sim_number):
    try:
        db = dbconfig()
        cursor = db.cursor()

        # Fetch the SIM card details
        cursor.execute('SELECT * FROM sim_card.info WHERE sim_number = %s;', (sim_number,))
        sim = cursor.fetchone()

        if sim is None:
            return jsonify({"error": "SIM card not found"}), 404

        # Convert row to a dictionary and return as JSON
        sim_details = {
            "sim_number": sim[0],
            "phone_number": sim[1],
            "status": sim[2],
            "activation_date": sim[3]
        }
        return jsonify(sim_details), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        db.close()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

