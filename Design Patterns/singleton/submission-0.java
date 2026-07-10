static class Singleton {

    private static Singleton instance = null;
    private String str = null;


    private Singleton() {
  
    }

    public static Singleton getInstance() {
        if (instance == null){
            instance = new Singleton();
        }
        return instance;
    }

    public String getValue() {
        return instance.str;
    }

    public void setValue(String value) {
        instance.str = value;
    }
    
}
