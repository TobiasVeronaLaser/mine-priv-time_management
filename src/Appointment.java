import java.time.LocalDateTime;

class Appointment{
    private String name;
    private String description;
    private LocalDateTime start, end;

    public Appointment(String name, String description, LocalDateTime start, LocalDateTime end){

    }

    public Appointment(){

    }

    public void setName(String name){
        this.name = name;
    }

    public void setDescription(String description){
        this.description = description;
    }

    public void setStart(LocalDateTime start){
        this.start = start;
    }

    public void setEnd(LocalDateTime end){
        this.end = end;
    }

    public String getName(){
        
    }


}