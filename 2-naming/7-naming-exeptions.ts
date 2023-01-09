class Database {
    private client: any;

    get connectedClient() {
        if(!this.client) {
            throw new Error('Database is not connected');
        }
        return this.client;
    }

    connect() {
        this.client = 'connected';
    }
}