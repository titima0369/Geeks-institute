from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



@app.route('/delete/<int:game_id>', methods=['POST'])
def delete_game(game_id):
    conn = None
    cursor = None
    
    try:
        # Connexion à PostgreSQL
        conn = get_db_connection()
        if not conn:
            flash('Erreur de connexion à la base de données', 'error')
            return redirect(url_for('index'))
        
        cursor = conn.cursor()
        
        # 1. Vérifier si le jeu existe et récupérer son titre
        cursor.execute("SELECT title FROM games WHERE id = %s", (game_id,))
        result = cursor.fetchone()
        
        if not result:
            flash('Jeu non trouvé.', 'error')
            return redirect(url_for('index'))
        
        game_title = result[0]
        
        # 2. Supprimer le jeu
        cursor.execute("DELETE FROM games WHERE id = %s", (game_id,))
        
        # 3. Vérifier si la suppression a réussi
        if cursor.rowcount > 0:
            conn.commit()
            flash(f'Le jeu "{game_title}" a été supprimé avec succès!', 'success')
        else:
            flash('Aucun jeu supprimé.', 'warning')
        
        return redirect(url_for('index'))  # Remplacez 'index' par votre route de liste
        
    except psycopg2.Error as e:
        # Erreur de base de données
        if conn:
            conn.rollback()
        flash(f'Erreur de base de données: {str(e)}', 'error')
        return redirect(url_for('index'))
        
    except Exception as e:
        # Autres erreurs
        if conn:
            conn.rollback()
        flash(f'Erreur inattendue: {str(e)}', 'error')
        return redirect(url_for('index'))
        
    finally:
        # Toujours fermer les connexions
        if cursor:
            cursor.close()
        if conn:
            conn.close()

