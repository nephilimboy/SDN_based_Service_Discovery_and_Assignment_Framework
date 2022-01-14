package apps.amirServiceChainPacketForwarder.src.main.java.org.onosproject.amirServiceChainPacketForwarder;

import org.onlab.graph.Edge;
import org.onlab.packet.Ethernet;
import org.onlab.packet.IpAddress;
import org.onosproject.core.ApplicationId;
import org.onosproject.net.*;
import org.onosproject.net.device.DeviceService;
import org.onosproject.net.device.PortStatistics;
import org.onosproject.net.flow.*;
import org.onosproject.net.flow.instructions.Instructions;
import org.onosproject.net.host.HostService;
import org.onosproject.net.topology.TopologyEdge;
import org.onosproject.net.topology.TopologyService;
import org.onosproject.net.topology.TopologyVertex;
import org.slf4j.Logger;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Integer.parseInt;


public class ControllerTask {

    public static final String MainVirtualHostIPAddress = "192.168.0.17";
    //    public static final String SourceIP = "10.10.0.1";
//    public static final String InitialDestinationIP = "10.10.0.2";
//    public static final String SecondDestinationIP = "10.10.0.3";
    public static final String InitialDestinationName = "5cc2";
    public static final String SecondDestinationName = "d4d8";
    public static final String[] WebServersName = {InitialDestinationName, SecondDestinationName};
    public static final int UpThreshold = 20;


    public static final Integer MinServersIPAddress = 100; //10.10.10.100
    public static final Integer MaxServersIPAddress = 200; //10.10.10.200
    public static final String MinVehicleIPAddress = "10.10.10.2";
    public static final String MaxVehicleIPAddress = "10.10.10.99";


    class Task extends TimerTask {

        public Device getDevice() {
            return device;
        }

        public DeviceService getDeviceService() {
            return deviceService;
        }

        public long getDelay() {
            return delay;
        }


        private Map<Path, Long> linkCostMap = new HashMap<Path, Long>();

        public void setLinkCostMap(Map<Path, Long> linkCostMap) {
            this.linkCostMap = linkCostMap;
        }

        public Map<Path, Long> getLinkCostMap() {
            return linkCostMap;
        }
        // <Name, ContainerOBJ>

        private Map<String, Vehicle> vehicleMap = new HashMap<String, Vehicle>();

        public Map<String, Vehicle> getVehicleMap() {
            return vehicleMap;
        }

        public void setVehicleMap(Map<String, Vehicle> vehicleMap) {
            this.vehicleMap = vehicleMap;
        }

        public Host REFHOST;

        public Host getREFHOST() {
            return REFHOST;
        }

        public void setREFHOST(Host REFHOST) {
            this.REFHOST = REFHOST;
        }

        // Previous link cost
        private long pathToInitDstPreviousBitSent = 0;

        private long pathToSecondDstPreviousBitSent = 0;


        // Previous Host and its flows
        private HostLocation previousLocation = null;


        public long[] getLinkStatusDeltaValues() {
            return linkStatusDeltaValues;
        }

        public HostLocation getPreviousLocation() {
            return previousLocation;
        }

        public void setPreviousLocation(HostLocation previousLocation) {
            this.previousLocation = previousLocation;
        }

        public class Server {
            private float cpu;
            private float memory;
            private String flavor;
            private Host physicalHost;

            public String getFlavor() {
                return flavor;
            }

            public void setFlavor(String flavor) {
                this.flavor = flavor;
            }

            public Host getPhysicalHost() {
                return physicalHost;
            }

            public void setPhysicalHost(Host physicalHost) {
                this.physicalHost = physicalHost;
            }

            public Server(Host host) {
                this.physicalHost = host;
            }

            public float getCpu() {
                return cpu;
            }

            public void setCpu(float cpu) {
                this.cpu = cpu;
            }

            public float getMemory() {
                return memory;
            }

            public void setMemory(float memory) {
                this.memory = memory;
            }
        }

        public class Vehicle {
            private Host vehicleHost;

            private Host vehiclePreviousHost;
            private Host vehicleNextHost;

            public Vehicle(Host car, Host previous, Host next) {
                this.vehicleHost = car;
                this.vehiclePreviousHost = previous;
                this.vehicleNextHost = next;
            }

            public Host getVehicleHost() {
                return vehicleHost;
            }

            public void setVehicleHost(Host vehicleHost) {
                this.vehicleHost = vehicleHost;
            }

            public Host getVehiclePreviousHost() {
                return vehiclePreviousHost;
            }

            public Host getVehicleNextHost() {
                return vehicleNextHost;
            }

            public void setVehiclePreviousHost(Host vehiclePreviousHost) {
                this.vehiclePreviousHost = vehiclePreviousHost;
            }

            public void setVehicleNextHost(Host vehicleNextHost) {
                this.vehicleNextHost = vehicleNextHost;
            }
        }

        @Override
        public void run() {

            log.info("***************************  VANET user assignment is running ****************************");
            log.info("*******************************************************************************************");


            while (!isExit()) {
                // Finding the servers and edge switches
                ArrayList<Device> edgeSwitchedConnectedToTheServers = new ArrayList<>();
                ArrayList<Host> edgeServers = new ArrayList<>();
                ArrayList<Server> serversNeighbors = new ArrayList<>();
                edgeSwitchedConnectedToTheServers.clear();
                edgeServers.clear();
                for (Host container : getHostService().getHosts()) {
                    // Servers
                    if (100 <= parseInt(container.ipAddresses().toString().split("10.10.10.")[1].split("]")[0])) {
                        edgeServers.add(container);
                        serversNeighbors.add(new Server(container));
                        if(101 == parseInt(container.ipAddresses().toString().split("10.10.10.")[1].split("]")[0])){
                            setREFHOST(container);
                        }
//                        for (Device dev: getDeviceService().getDevices()){
//                            if (container.location().deviceId().toString().equals(dev.id().toString())){
//                                edgeSwitchedConnectedToTheServers.add(dev);
//                            }
//                        }
                    }
                }

                // Check if the car's location is about to change
                for (Host container : getHostService().getHosts()) {
                    // Cars
                    if (2 <= parseInt(container.ipAddresses().toString().split("10.10.10.")[1].split("]")[0]) &&
                            parseInt(container.ipAddresses().toString().split("10.10.10.")[1].split("]")[0]) < 100) {
                        log.info("------ Vehicle's IP address " + container.ipAddresses().toString() + " --------------------");
                        if (getVehicleMap().containsKey(container.ipAddresses().toString())) {
                            log.info("[*] Check the vehicle's location");
                            if (getVehicleMap().get(container.ipAddresses().toString()).getVehicleHost() == null || !container.location().deviceId().toString().equals(getVehicleMap().get(container.ipAddresses().toString()).vehicleHost.location().deviceId().toString())) {
                                log.info("[*] Vehicle location has changed");
                                // save the location of the vehicle
                                getVehicleMap().get(container.ipAddresses().toString()).setVehicleHost(container);
                                ///////////////////////////////////////////////////////////////////////////////////////
//                                Map<DeviceId, int> AllShortestPath = new HashMap<DeviceId, int>();
//                                for (Host service: edgeServers){
//                                    Set<Path> paths =
//                                            topologyService.getPaths(topologyService.currentTopology(),
//                                                    container.location().deviceId(),
//                                                    service.location().deviceId());
//                                    if(paths.size() > 0){
//                                        for (Path pp:paths){
//                                            AllShortestPath.put(service.location().deviceId(), pp.links().size() );
//                                            break;
//                                        }
//                                    }
//                                }
//                                int numberOfLinks = 0;
//                                for (int num: AllShortestPath.values()){
//                                    if (numberOfLinks == 0){
//                                        numberOfLinks = num;
//                                    }
//                                    else if(num < numberOfLinks) {
//                                        numberOfLinks = num;
//                                    }
//                                }


                                ///////////////////////////////////////////////////////////////////////////////////////


//                                // Find all nearby edge switch of the car's location
//                                ArrayList<TopologyVertex> deviceNeighbors = new ArrayList<>();
//                                log.info("[*] Find the nearby switches");
//                                // Save the connected switch itself to as a nearby switch
//                                //TODO replace "TopologyVertex" with "DeviceID" to prevent below loop
//                                for (TopologyVertex vertex : getTopologyService().getGraph(getTopologyService().currentTopology()).getVertexes()) {
//                                    if (vertex.deviceId().toString().equals(container.location().deviceId().toString())) {
//                                        deviceNeighbors.add(vertex);
//                                    }
//                                }
//                                // Save the nearby switches
//                                for (TopologyEdge edge : getTopologyService().getGraph(getTopologyService().currentTopology()).getEdges()) {
//                                    if (edge.src().toString().equals(container.location().deviceId().toString())) {
//                                        log.info("      -> Switch ID: " + edge.dst().toString());
//                                        deviceNeighbors.add(edge.dst());
//                                    }
//                                }
//                                // Find all services in nearby
//                                ArrayList<Server> serversNeighbors = new ArrayList<>();
//                                log.info("[*] Find nearby services");
//                                for (Host aService : getHostService().getHosts()) {
//                                    if (MinServersIPAddress <= parseInt(aService.ipAddresses().toString().split("10.10.10.")[1].split("]")[0]) &&
//                                            parseInt(aService.ipAddresses().toString().split("10.10.10.")[1].split("]")[0]) < MaxServersIPAddress) {
//                                        for (TopologyVertex nearbyServers : deviceNeighbors) {
//                                            if (aService.location().deviceId().equals(nearbyServers.deviceId())) {
//                                                log.info("      -> Service " + aService.ipAddresses().toString() + " connected to the switch " + aService.location().deviceId().toString());
//                                                serversNeighbors.add(new Server(aService));
//                                            }
//                                        }
//                                    }
//                                }
                                log.info("[*] Get utilization of nearby services");
                                // Get the utilization of all nearby services
                                float smalletUtil = 0;
                                Server bestServer = null;
                                try {
                                    for (Server server : serversNeighbors) {
                                        float tempCpu = -1;
                                        float tempMemory = -1;
                                        URL URLapp = new URL("http://" + MainVirtualHostIPAddress + "/10.10.10." + server.getPhysicalHost().ipAddresses().toString().split("10.10.10.")[1].split("]")[0]);
                                        BufferedReader in = new BufferedReader(
                                                new InputStreamReader(URLapp.openStream()));
                                        String inputLine;
                                        while ((inputLine = in.readLine()) != null) {
                                            if (inputLine.startsWith("Cpu")) {
                                                tempCpu = Float.parseFloat(inputLine.split(" ")[1].replace("%", ""));
                                            } else if (inputLine.startsWith("MemoryUsage")) {
                                                tempMemory = Float.parseFloat(inputLine.split(" ")[1].replace("%", ""));
                                            }
                                        }
                                        in.close();
                                        if (tempCpu >= 0 && tempMemory >= 0) {
                                            server.setCpu(tempCpu);
                                            server.setMemory(tempMemory);
                                            if (smalletUtil == 0) {
                                                smalletUtil = tempCpu + tempMemory;
                                                bestServer = server;
                                            } else if (smalletUtil >= tempCpu + tempMemory) {
                                                smalletUtil = tempCpu + tempMemory;
                                                bestServer = server;
                                            }
//                                            log.info("      -> Service " + server.getPhysicalHost().ipAddresses().toString() + " :" + " CPU " + String.valueOf(tempCpu) + " Memory " + String.valueOf(tempMemory));
                                        }
                                    }
                                } catch (IOException e) {
                                    log.error(e.toString());
                                }
                                log.info("-> best server ip address is: " + bestServer.getPhysicalHost().ipAddresses().toString());
                                getVehicleMap().get(container.ipAddresses().toString()).setVehicleNextHost(bestServer.getPhysicalHost());

                                if(getVehicleMap().get(container.ipAddresses().toString()).getVehicleNextHost() != null
//                                        && !getVehicleMap().get(container.id()).getVehiclePreviousHost().id().toString().equals(getVehicleMap().get(container.id()).getVehicleNextHost().id().toString())
                                ){
                                    if(getREFHOST().id() != null){

//                                        installRule(container, container.location(), getREFHOST(), getVehicleMap().get(container.ipAddresses().toString()).getVehicleNextHost());
                                    }
                                    else{
                                        log.info("REF HOST is empty");
                                    }
                                }
                                else{
                                    log.info("[*] Error detected");
                                }
                                // REFHOST is used instead
//                                getVehicleMap().get(container.ipAddresses().toString()).setVehiclePreviousHost(getVehicleMap().get(container.ipAddresses().toString()).getVehicleNextHost());




//                                for (Server sererr : serversNeighbors) {
//                                    if (   parseInt(sererr.getPhysicalHost().ipAddresses().toString().split("10.10.10.")[1].split("]")[0]) == 101){
//                                        log.info("Init Server " + sererr.getPhysicalHost().ipAddresses().toString());
//                                        log.info("Destination Server " + bestServer.getPhysicalHost().ipAddresses().toString());
//                                        log.info("Car location" + container.location().toString());
//                                        installRule(container.location(), sererr.getPhysicalHost(), bestServer.getPhysicalHost());
//                                        break;
//                                    }
//                                }


                                // Shortest path to each nearby services
//                                log.info("[*] Get utilization of the shortest path to nearby services");
//                                for (Server server : serversNeighbors) {
//                                    Set<Path> pathsToService =
//                                            getTopologyService().getPaths(getTopologyService().currentTopology(),
//                                                    container.location().deviceId(),
//                                                    server.physicalHost.location().deviceId());
//                                    long pathToServiceBitSentPerSecond = 0;
//                                    for (Path pathToDst : pathsToService) {
//                                        long cumulativeCost = 0;
//                                        for (Link lk : pathToDst.links()) {
//                                            cumulativeCost = cumulativeCost + getDeviceService().getStatisticsForPort(lk.src().deviceId(), lk.src().port()).bytesReceived();
//                                        }
//                                        pathToServiceBitSentPerSecond = cumulativeCost;
//                                        break;
//                                    }
//                                    log.info("      -> Path to service " + server.getPhysicalHost().ipAddresses().toString() + " :" + " Utilization " + String.valueOf(pathToServiceBitSentPerSecond) + " byte ");
//                                }
                                log.info("[*] Get utilization of the shortest path to nearby services");
                                for (Server server : serversNeighbors) {
                                    Set<Path> pathsToService =
                                            getTopologyService().getPaths(getTopologyService().currentTopology(),
                                                    container.location().deviceId(),
                                                    server.physicalHost.location().deviceId());
//                                    long pathToServiceBitSentPerSecond = 0;
                                    for (Path pathToDst : pathsToService) {
                                        long minimumCost = 0;
                                        for (Link lk : pathToDst.links()) {
                                            if (minimumCost == 0){
                                                minimumCost = getDeviceService().getStatisticsForPort(lk.src().deviceId(), lk.src().port()).bytesReceived();
                                            }
                                            if(minimumCost > getDeviceService().getStatisticsForPort(lk.src().deviceId(), lk.src().port()).bytesReceived()){
                                                minimumCost = getDeviceService().getStatisticsForPort(lk.src().deviceId(), lk.src().port()).bytesReceived();
                                            }

                                        }
                                        getLinkCostMap().put(pathToDst, minimumCost/3);
                                    }


                                    // IN EACH PATH see each segment and see what is the available bit that i can use
                                    
                                    long minPath = 0;
                                    for (Map.Entry<Path, Long> lCost: getLinkCostMap().entrySet()){
                                        if(minPath == 0 ){
                                            minPath = lCost.getValue();
                                        }
                                        if(minPath > lCost.getValue()){
                                            minPath = lCost.getValue();
                                        }
                                    }
                                    Path SelectedPath = null;
                                    for (Map.Entry<Path, Long> lCost: getLinkCostMap().entrySet()){
                                        if(minPath == lCost.getValue()){
                                            SelectedPath = lCost.getKey();
                                        }
                                    }

                                    log.info("      -> Path to service " + server.getPhysicalHost().ipAddresses().toString() + " is: " + SelectedPath.toString() + " with Utilization " + minPath + " byte/sec ");

                                }


                            }
                        } else {
                            log.info("Monitor vehicle with IP address: " + container.id().toString());
                            getVehicleMap().put(container.ipAddresses().toString(), new Vehicle(null, null, null));

                            String mapAsString =  getVehicleMap().keySet().stream()
                                    .map(key -> key + "=" + getVehicleMap().get(key))
                                    .collect(Collectors.joining(", ", "{", "}"));
                            log.info("my map is  " +  mapAsString);
                        }
                    }

                }

                ////////////////////////////////////////////////////////////////////////////////////////////////////////
                ////////////////////////////////////////////////////////////////////////////////////////////////////////


//                if (WebServersName.length == getContainerMap().size()) {
//                    log.info("----------- Collecting servers' utilization ---------------------------");
//                    containerMap.forEach((key, value) -> {
//                        if(key.equals(InitialDestinationName))
//                            log.info("Service 10.10.0.2 utilization is " + String.valueOf(value.getCpu()));
//                        else
//                            log.info("Service 10.10.0.3 utilization is " + String.valueOf(value.getCpu()));
//                    });
//
//                    // Both destination Host
//                    Host initialDestinationHost = null;
//                    Host secondDestinationHost = null;
//                    boolean findInitHost = false;
//                    boolean findSecondHost = false;
//
//
//                    for (Host host : getHostService().getHostsByIp(IpAddress.valueOf(InitialDestinationIP))) {
//                        initialDestinationHost = host;
////                        log.info("initialDestinationHost: " + initialDestinationHost.toString());
//                        findInitHost = true;
//                    }
//                    for (Host host : getHostService().getHostsByIp(IpAddress.valueOf(SecondDestinationIP))) {
//                        secondDestinationHost = host;
////                        log.info("secondDestinationHost: " + secondDestinationHost.toString());
//                        findSecondHost = true;
//                    }
//
//
//                    // Check both destination are found
//                    if (findSecondHost && findInitHost) {
//
////                    log.info("Both destination hosts are founded");
//
//                        for (Host host : getHostService().getHostsByIp(IpAddress.valueOf(SourceIP))) {
////                        log.info("Source host has been founded");
//                            if (getPreviousLocation() == null) {
//                                setPreviousLocation(host.location());
////                            installRule(host.location(), initialDestinationHost, secondDestinationHost);
//                            } else {
//                                // Has vehicle's location changed?
//                                if (!getPreviousLocation().deviceId().toString().equals(host.location().deviceId().toString())) {
//                                    log.info("----------- Vehicle's location has changed -------------------------------");
//                                    // Check the Utilization of the second host
//                                    if (containerMap.get(SecondDestinationName).getCpu() < UpThreshold) {
////                                    if (true) {
//                                        log.info("----------- Collecting user data size (bit rate per second) -----------");
//                                        // Calculate the ROUTING ALGORITHMS WITH DYNAMIC LINK COST(RA-DLC)
//                                        // The shortest path to the service in zone 2 (newPath)
//                                        Set<Path> pathsToSecondHost =
//                                                getTopologyService().getPaths(getTopologyService().currentTopology(),
//                                                        host.location().deviceId(),
//                                                        secondDestinationHost.location().deviceId());
//
//                                        // The shortest path to the service in zone 1 (prevPath)
//                                        Set<Path> pathsToInitialHost =
//                                                getTopologyService().getPaths(getTopologyService().currentTopology(),
//                                                        host.location().deviceId(),
//                                                        initialDestinationHost.location().deviceId());
//
//                                        long pathToInitDstPreviousBitSentPerSecond = 0;
//                                        long pathToSecondDstPreviousBitSentPerSecond = 0;
//
//                                        for (Path pathToInitDst : pathsToInitialHost) {
//                                            long cumulativeCost = 0;
//                                            for (Link lk : pathToInitDst.links()) {
//                                                cumulativeCost = cumulativeCost + getDeviceService().getStatisticsForPort(lk.src().deviceId(), lk.src().port()).bytesSent();
//                                            }
//                                            if(pathToInitDstPreviousBitSent != cumulativeCost) {
//                                                pathToInitDstPreviousBitSentPerSecond = (cumulativeCost - pathToInitDstPreviousBitSent) / 3;
//                                                pathToInitDstPreviousBitSent = cumulativeCost;
//                                            }
//                                            break;
//                                        }
//                                        for (Path pathToSecondDst : pathsToSecondHost) {
//                                            long cumulativeCost = 0;
//                                            for (Link lk : pathToSecondDst.links()) {
//                                                cumulativeCost = cumulativeCost + getDeviceService().getStatisticsForPort(lk.src().deviceId(), lk.src().port()).bytesSent();
//                                            }
//                                            if(pathToSecondDstPreviousBitSent != cumulativeCost) {
//                                                pathToSecondDstPreviousBitSentPerSecond = (cumulativeCost - pathToSecondDstPreviousBitSent) / 3;
//                                                pathToSecondDstPreviousBitSent = cumulativeCost;
//                                            }
//                                            break;
//                                        }
//
//                                        log.info("Bit rate of the path to 10.10.0.2: " + pathToInitDstPreviousBitSentPerSecond + " bit/sec");
//                                        log.info("Bit rate of the path to 10.10.0.3: " + pathToSecondDstPreviousBitSentPerSecond + " bit/sec");
//                                        log.info("--------------------------------------------------------------------------");
//
//                                        if (pathToSecondDstPreviousBitSentPerSecond < 10 * pathToInitDstPreviousBitSentPerSecond) {
////                                        if (true) {
//                                            log.info("Assigning the vehicle to service in zone 2 (10.10.0.3)");
//                                            // Remove rules from previous host
//                                            log.info("Removing rules from previous switch");
//                                            for (FlowRule flowRl : previousHostFlowRules) {
//                                                flowRuleService.removeFlowRules(flowRl);
//                                            }
//                                            previousHostFlowRules.clear();
//
//                                            // Set the new flow on new edge switch
//                                            log.info("Adding rules to the new switch");
//                                            installRule(host.location(), initialDestinationHost, secondDestinationHost);
//
//                                            // At the end remove the previous host and add new host to it
//                                            log.info("Update the vehicle location in database");
//                                            setPreviousLocation(host.location());
//                                        }
//                                    }
//                                }
//                            }
//                        }
//                    }
//                }

                try {
                    Thread.sleep((getDelay() * 1000));
                    break;
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

            }
        }
    }


    long[] linkStatusDeltaValues = new long[2];

    public void setLinkStatusDeltaValues(long[] linkStatusDeltaValues) {
        this.linkStatusDeltaValues = linkStatusDeltaValues;
    }

    private Set<FlowRule> previousHostFlowRules = new HashSet<>();

    void installRule(Host vehivle, HostLocation hostLocation, Host initialHostDestination, Host secondHostDestination) {
        log.info("  ############# ############# ############# ############# ############# ############# #############");
        log.info("  ############# ############# Setting new role ############# ############# #############");

        IpAddress secDestIp = null;
        IpAddress initDestIp = null;
        for (IpAddress ipSec : secondHostDestination.ipAddresses()) {
            secDestIp = ipSec;
            break;
        }
        for (IpAddress ipInit : initialHostDestination.ipAddresses()) {
            initDestIp = ipInit;
            break;
        }

        log.info("Installing rules.....");
        Set<Path> paths =
                getTopologyService().getPaths(getTopologyService().currentTopology(),
                        hostLocation.deviceId(),
                        secondHostDestination.location().deviceId());

        Path mainPath = paths.stream().findFirst().get();

        // First Rule (Transmission)
        TrafficSelector selectorSending = DefaultTrafficSelector.builder()
                .matchEthType(Ethernet.TYPE_IPV4)
                .matchInPort(hostLocation.port())
                .matchEthSrc(vehivle.mac())
                .build();
        TrafficTreatment treatmentSending = DefaultTrafficTreatment.builder()
                .add(Instructions.modL2Dst(secondHostDestination.mac()))
//                .add(Instructions.modL3Dst(IpAddress.valueOf(SecondDestinationIP)))
                .add(Instructions.modL3Dst(secDestIp))
                .setOutput(mainPath.src().port())
                .build();
        FlowRule flowRuleSending = DefaultFlowRule.builder()
                .forDevice(hostLocation.deviceId())
                .fromApp(getAppId())
                .withSelector(selectorSending)
                .withTreatment(treatmentSending)
                .withPriority(60010)
                .makePermanent()
                .build();
        FlowRuleOperations flowRuleOperationsSending = FlowRuleOperations.builder()
                .add(flowRuleSending)
                .build();
        flowRuleService.apply(flowRuleOperationsSending);


        // Second Rule (Receiving)
        TrafficSelector selectorReceiving = DefaultTrafficSelector.builder()
                .matchEthType(Ethernet.TYPE_IPV4)
                .build();
        TrafficTreatment treatmentReceiving = DefaultTrafficTreatment.builder()
                .add(Instructions.modL2Src(initialHostDestination.mac()))
//                .add(Instructions.modL3Src(IpAddress.valueOf(InitialDestinationIP)))
                .add(Instructions.modL3Src(initDestIp))
                .setOutput(hostLocation.port())
                .build();
        FlowRule flowRuleReceiving = DefaultFlowRule.builder()
                .forDevice(hostLocation.deviceId())
                .fromApp(getAppId())
                .withSelector(selectorReceiving)
                .withTreatment(treatmentReceiving)
                .withPriority(60009)
                .makePermanent()
                .build();
        FlowRuleOperations flowRuleOperationsReceiving = FlowRuleOperations.builder()
                .add(flowRuleReceiving)
                .build();
        flowRuleService.apply(flowRuleOperationsReceiving);


        previousHostFlowRules.add(flowRuleSending);
        previousHostFlowRules.add(flowRuleReceiving);
    }

    private long calculateBitrate(long numberOfBit) {
        if (linkStatusDeltaValues.length == 0) {

        }
        return 0L;
    }

    private FlowRuleService flowRuleService;

    public FlowRuleService getFlowRuleService() {
        return flowRuleService;
    }

    public void setFlowRuleService(FlowRuleService flowRuleService) {
        this.flowRuleService = flowRuleService;
    }

    private Iterable<FlowEntry> flowEntries;

    public Iterable<FlowEntry> getFlowEntries() {
        return flowEntries;
    }

    public void setFlowEntries(Iterable<FlowEntry> flowEntries) {
        this.flowEntries = flowEntries;
    }

    private PortNumber portNumber;

    public PortNumber getPortNumber() {
        return portNumber;
    }

    public void setPortNumber(PortNumber portNumber) {
        this.portNumber = portNumber;
    }

    public void schedule() {
        this.getTimer().schedule(new Task(), 0, 1000);
    }

    public Timer getTimer() {
        return timer;
    }

    public void setTimer(Timer timer) {
        this.timer = timer;
    }

    private Timer timer = new Timer();

    public Logger getLog() {
        return log;
    }

    public void setLog(Logger log) {
        this.log = log;
    }

    private Logger log;

    public boolean isExit() {
        return exit;
    }

    public void setExit(boolean exit) {
        this.exit = exit;
    }

    private boolean exit;

    public long getDelay() {
        return delay;
    }

    public void setDelay(long delay) {
        this.delay = delay;
    }

    private long delay;

    public PortStatistics getPortStats() {
        return portStats;
    }

    public void setPortStats(PortStatistics portStats) {
        this.portStats = portStats;
    }

    private PortStatistics portStats;

    public Long getPort() {
        return port;
    }

    public void setPort(Long port) {
        this.port = port;
    }

    private Long port;

    public DeviceService getDeviceService() {
        return deviceService;
    }

    public void setDeviceService(DeviceService deviceService) {
        this.deviceService = deviceService;
    }

    protected DeviceService deviceService;

    public Device getDevice() {
        return device;
    }

    public void setDevice(Device device) {
        this.device = device;
    }


    protected HostService hostService;

    public void setHostService(HostService hostService) {
        this.hostService = hostService;
    }

    public HostService getHostService() {
        return hostService;
    }


    protected TopologyService topologyService;

    public void setTopologyService(TopologyService topologyService) {
        this.topologyService = topologyService;
    }

    public TopologyService getTopologyService() {
        return topologyService;
    }

    private ApplicationId appId;

    public ApplicationId getAppId() {
        return appId;
    }

    public void setAppId(ApplicationId appId) {
        this.appId = appId;
    }

    private Device device;
}

