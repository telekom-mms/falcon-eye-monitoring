# Known bugs and problems

- [Grafana](#grafana)  
- [Opensearch](#opensearch)  

## Grafana

The current Grafana has problems with huge jaeger traces which results in React errors. 

```
Error: Minified React error #185; visit https://reactjs.org/docs/error-decoder.html?invariant=185 for the full message or use the non-minified dev environment for full errors and additional helpful warnings.
```

If your are facing the problem described above you have to go back to version 9.0.2

## Opensearch

If there are many traces indexed and your are facing problems while querying traces it might be neccessary to define `-XX:NewSize` jvm parameter.