findGradient = function (coordinateA, coordinateB)
    {
        let gradient = (coordinateA[1]-coordinateB[1])/(coordinateA[0]-coordinateB[0]);
        return +gradient.toFixed(2);
    }

    checkStraightLine = function(coordinates) {
    
    
        if(coordinates[0][0] === 0 && coordinates[0][1] === 0)
        {
            coordinates.shift();
        }
        
        if(coordinates.length === 2)
        {
            return true;
        }
               
        let gradient = this.findGradient(coordinates[0],coordinates[1]);
            
        for(let i = 1; i < coordinates.length-1; i++)
        {
            if(gradient != this.findGradient(coordinates[i],coordinates[i+1]))
            {
                return false
            }
        }
        
        return true;
        
    };