        hour= hour*30;
        double min;
        int minsp;
        min= minutes*0.5;
        minsp= minutes*6;
        
        res= abs((hour+min)-minsp);
        double minre;
        minre=360-res;
         return (minre>res)?res:minre;
    }