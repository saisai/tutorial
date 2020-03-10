<?php

class CreateTableDemo {
    
    const DB_HOST = "localhost";

    const DB_NAME = "classicmodels";

    const DB_USER = "root";

    const DB_PASSWORD = "root";

    private $pdo = null;


    // open the database connection
    public function __construct() {

        $conStr = sprintf("mysql:host=%s;dbname=%s", self::DB_HOST, self::DB_NAME);

        try {
            $this->pdo = new PDO($conStr, self::DB_USER, self::DB_PASSWORD);
        } catch (PDOException $e) {

            echo $e->getMessage();
            
            }

    }



    public function createTaskTable() {
        
        $sql = <<<EOSQL
            CREATE TABLE IF NOT EXISTS tasks (
            task_id     INT AUTO_INCREMENT PRIMARY KEY,
            subject     VARCHAR(255)        DEFAULT NULL,
            start_date  DATE                DEFAULT NULL,
            end_date    DATE                DEFAULT NULL,
            description VARCHAR(400)        DEFAULT NULL
            );
EOSQL;
        return $this->pdo->exec($sql);
		
		//var_dump($this->pdo);

    }
	
    // close the database connection
    public function __destruct()
    {
        $this->pdo = null;
    }	

}

// create the tasks table
$obj = new CreateTableDemo();
$obj->createTaskTable();
