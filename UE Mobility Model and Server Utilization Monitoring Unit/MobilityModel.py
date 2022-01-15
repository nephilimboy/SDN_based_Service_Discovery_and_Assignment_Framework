import json
import random
import time
from multiprocessing import Process
from subprocess import call
import queue
from threading import Thread, Event
from argparse import ArgumentParser
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random as npRand
import requests
from subprocess import PIPE, run


Topology = '''
{ "class": "go.GraphLinksModel",
  "copiesArrays": true,
  "copiesArrayObjects": true,
  "linkFromPortIdProperty": "fromPort",
  "linkToPortIdProperty": "toPort",
  "nodeDataArray": [ 
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#949a0f34-eb36-4c54-a021-304e7880a246", "name":"Switch", "describtion":"S#eb36", "loc":"682.6655720848155 -398.6860104091251", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#7cdb9f0d-8ec2-4e3a-85be-edb76f7ca704", "name":"Switch", "describtion":"S#8ec2", "loc":"698.9195142773115 -171.1308197141866", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#cbe82348-a333-4113-841c-456879496d4c", "name":"Switch", "describtion":"S#a333", "loc":"684.9875638266008 72.67831317324749", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#21869922-1615-4ce5-9b2e-4ae4d91e2a74", "name":"Switch", "describtion":"S#1615", "loc":"701.241506019096 307.1994790935413", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#2f2b1b88-8490-4eb1-b648-d4120fa4a4e0", "name":"Switch", "describtion":"S#8490", "loc":"705.8854895026666 532.432678046695", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#c78e82d5-a936-4d6a-9f31-e9ee3fb5f39b", "name":"Switch", "describtion":"S#a936", "loc":"436.53444745559614 88.93225536574312", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#9b4c1d7b-9dda-49dd-a227-74d4430526c0", "name":"Switch", "describtion":"S#9dda", "loc":"243.8091328874341 93.57623884931331", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#d047857d-020c-4829-8313-b39fe29b55de", "name":"Switch", "describtion":"S#020c", "loc":"62.693777028197474 93.57623884931331", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#2d3935c3-133a-4cc1-b1bd-8b7b25b1d31d", "name":"Switch", "describtion":"S#133a", "loc":"-120.74357057282452 93.57623884931331", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#3e03439d-d532-42df-ac30-c409b711f2be", "name":"Switch", "describtion":"S#d532", "loc":"487.6182657748682 541.7206450138349", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#1c2acfd0-5e71-4490-b262-cbf462e8611a", "name":"Switch", "describtion":"S#5e71", "loc":"276.31701727242535 541.7206450138351", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#35972182-108f-4157-af84-e1bed2d97c30", "name":"Switch", "describtion":"S#108f", "loc":"81.26971096247803 541.7206450138351", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#72f5a3f8-d534-4325-b637-b1c283a669e3", "name":"Switch", "describtion":"S#d534", "loc":"-109.13361186389909 518.5007275959842", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#24cec8cc-4247-4d68-9065-8f751685e0a7", "name":"Switch", "describtion":"S#4247", "loc":"-304.1809181738464 -412.61796085983565", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#ce097b94-f6ce-4995-b618-273cb5f0d837", "name":"Switch", "describtion":"S#f6ce", "loc":"-301.85892643206114 -173.45281145597164", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#fa3dd258-eb9d-4252-b4f9-2bd7a1b75bb4", "name":"Switch", "describtion":"S#eb9d", "loc":"-297.21494294849117 70.35632143146256", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#6bb109ce-52de-4de0-8e1d-8d1d7316e618", "name":"Switch", "describtion":"S#52de", "loc":"-292.570959464921 304.87748735175614", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"a15c52b870f16fdd1aa8a285277ad985.png", "key":"Switch#ffbe75b4-6ac9-4fb6-9dde-d81c6a752e80", "name":"Switch", "describtion":"S#6ac9", "loc":"-299.536934690276 530.1106863049099", "serverId":2, "category":"Node", "controllerIp":"192.168.0.15", "controllerPort":"6653", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#316571", "portId":"eth0"} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#bbb332c7-ff0d-4921-87a8-534fb5892bd2", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#ff0d", "loc":"777.9406694660858 -403.08089611645886", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.101", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#9ca6ad9a-1928-499a-a9ba-06f92fb60349", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#1928", "loc":"797.1688546670551 -174.40214976519994", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.102", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#5fc6d318-23a7-482c-87f2-ba79fc8ad92c", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#23a7", "loc":"809.7011471275649 54.32928235985844", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.103", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#f435e8e7-8e6e-47c6-a976-cd151b575ffb", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#8e6e", "loc":"830.6545964062822 298.2872989620638", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.104", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#1d0c699b-fd32-4f82-b908-f75910acda9b", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#fd32", "loc":"847.1180208395596 527.2785660794713", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.105", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#6b508265-6d28-4856-9cc7-ec1af3b10153", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#6d28", "loc":"489.87304795016917 -117.4445418233739", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.106", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#06faf598-8b4b-483c-a0e2-b75c16765dc5", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#8b4b", "loc":"304.8821918266773 -114.8646956197349", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.107", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#f39508f0-81a7-439d-942f-f77219bec86f", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#81a7", "loc":"116.91619332468531 -108.46449213249517", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.108", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#9d518b33-0b8e-4433-8b02-2a5b4018edf4", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#0b8e", "loc":"-129.8921476424266 -127.40893872569643", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.109", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#fb674603-49f4-4d3b-81c9-dda7aef730aa", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#49f4", "loc":"-410.64809972445585 -415.2750701194321", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.110", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#612e29ac-d7f3-4c2e-880b-240eec9a4e37", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#d7f3", "loc":"-422.0103475315429 -165.2575236494709", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.111", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#3723cb88-7d50-495d-9c7b-1ac9ad76693b", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#7d50", "loc":"-413.97433678947993 75.05178978668579", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.112", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#5604bc84-4f12-4f89-8aed-bb3819430532", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#4f12", "loc":"-407.1021138278323 313.2714840120705", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.113", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#f8e0255a-4a3b-45e2-b66f-4700cde7f272", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#4a3b", "loc":"-398.53556783027403 544.501923713633", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.114", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#047a4503-ba57-4446-9ec7-1920f08b2693", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#ba57", "loc":"-152.83706177900427 763.6978317436656", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.115", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#5e078379-11fe-453c-8a64-e0f4a83c3b9f", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#11fe", "loc":"29.30174130198543 766.173309131401", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.116", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#14b04bab-649a-443c-93f2-63ab8e3dc634", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#649a", "loc":"220.82458142469204 760.704481846706", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.117", "gateway":""} ], "rightArray":[]},
{"source":"cf3c74def4b54aec86e789d4cc9441a2.png", "key":"VNF#de6ef9e8-ebba-4766-9ec9-c722d92e37b6", "name":"VNF", "imgName":"nephilimboy/httpd_3file_final", "executionCommand":" ", "describtion":"V#ebba", "loc":"429.100948173128 760.5508385366956", "cpu":"0", "ram":"0", "isDedicatedRes":"0", "serverId":2, "category":"Node", "leftArray":[], "topArray":[], "bottomArray":[ {"portColor":"#425e5c", "portId":"eth0", "name":"eth0", "ipAddress":"10.10.10.118", "gateway":""} ], "rightArray":[]}
 ],
  "linkDataArray": [ 
{"from":"Switch#2f2b1b88-8490-4eb1-b648-d4120fa4a4e0", "to":"Switch#3e03439d-d532-42df-ac30-c409b711f2be", "fromPort":"eth0", "toPort":"eth0", "points":[705.8854895026666,664.432678046695,705.8854895026666,674.432678046695,705.8854895026666,683.7206450138349,596.7518776387674,683.7206450138349,487.6182657748682,683.7206450138349,487.6182657748682,673.7206450138349]},
{"from":"Switch#1c2acfd0-5e71-4490-b262-cbf462e8611a", "to":"Switch#3e03439d-d532-42df-ac30-c409b711f2be", "fromPort":"eth0", "toPort":"eth0", "points":[276.31701727242535,673.7206450138351,276.31701727242535,683.7206450138351,487.6182657748682,683.7206450138351,487.6182657748682,683.720645013835,487.6182657748682,683.7206450138349,487.6182657748682,673.7206450138349]},
{"from":"Switch#35972182-108f-4157-af84-e1bed2d97c30", "to":"Switch#1c2acfd0-5e71-4490-b262-cbf462e8611a", "fromPort":"eth0", "toPort":"eth0", "points":[81.26971096247803,673.7206450138351,81.26971096247803,683.7206450138351,276.31701727242535,683.7206450138351,276.31701727242535,683.7206450138351,276.31701727242535,683.7206450138351,276.31701727242535,673.7206450138351]},
{"from":"Switch#72f5a3f8-d534-4325-b637-b1c283a669e3", "to":"Switch#35972182-108f-4157-af84-e1bed2d97c30", "fromPort":"eth0", "toPort":"eth0", "points":[-109.13361186389909,650.5007275959842,-109.13361186389909,660.5007275959842,-109.13361186389909,683.7206450138351,-13.93195045071053,683.7206450138351,81.26971096247803,683.7206450138351,81.26971096247803,673.7206450138351]},
{"from":"Switch#ffbe75b4-6ac9-4fb6-9dde-d81c6a752e80", "to":"Switch#72f5a3f8-d534-4325-b637-b1c283a669e3", "fromPort":"eth0", "toPort":"eth0", "points":[-299.536934690276,662.1106863049099,-299.536934690276,672.1106863049099,-109.13361186389909,672.1106863049099,-109.13361186389909,666.3057069504471,-109.13361186389909,660.5007275959842,-109.13361186389909,650.5007275959842]},
{"from":"Switch#6bb109ce-52de-4de0-8e1d-8d1d7316e618", "to":"Switch#ffbe75b4-6ac9-4fb6-9dde-d81c6a752e80", "fromPort":"eth0", "toPort":"eth0", "points":[-292.570959464921,436.87748735175614,-292.570959464921,446.87748735175614,-292.570959464921,446.87748735175614,-244,446.87748735175614,-244,676,-299.536934690276,676,-299.536934690276,672.1106863049099,-299.536934690276,662.1106863049099]},
{"from":"Switch#fa3dd258-eb9d-4252-b4f9-2bd7a1b75bb4", "to":"Switch#6bb109ce-52de-4de0-8e1d-8d1d7316e618", "fromPort":"eth0", "toPort":"eth0", "points":[-297.21494294849117,202.35632143146256,-297.21494294849117,212.35632143146256,-297.21494294849117,212.35632143146256,-348,212.35632143146256,-348,444,-292.570959464921,444,-292.570959464921,446.87748735175614,-292.570959464921,436.87748735175614]},
{"from":"Switch#ce097b94-f6ce-4995-b618-273cb5f0d837", "to":"Switch#fa3dd258-eb9d-4252-b4f9-2bd7a1b75bb4", "fromPort":"eth0", "toPort":"eth0", "points":[-301.85892643206114,-41.45281145597164,-301.85892643206114,-31.45281145597164,-347.71494294849117,-31.45281145597164,-347.71494294849117,212.35632143146256,-297.21494294849117,212.35632143146256,-297.21494294849117,202.35632143146256]},
{"from":"Switch#24cec8cc-4247-4d68-9065-8f751685e0a7", "to":"Switch#ce097b94-f6ce-4995-b618-273cb5f0d837", "fromPort":"eth0", "toPort":"eth0", "points":[-304.1809181738464,-280.61796085983565,-304.1809181738464,-270.61796085983565,-352.35892643206114,-270.61796085983565,-352.35892643206114,-31.45281145597164,-301.85892643206114,-31.45281145597164,-301.85892643206114,-41.45281145597164]},
{"from":"Switch#2d3935c3-133a-4cc1-b1bd-8b7b25b1d31d", "to":"Switch#fa3dd258-eb9d-4252-b4f9-2bd7a1b75bb4", "fromPort":"eth0", "toPort":"eth0", "points":[-120.74357057282452,225.5762388493133,-120.74357057282452,235.5762388493133,-120.74357057282452,236,-172,236,-172,228,-297.21494294849117,228,-297.21494294849117,212.35632143146256,-297.21494294849117,202.35632143146256]},
{"from":"Switch#d047857d-020c-4829-8313-b39fe29b55de", "to":"Switch#2d3935c3-133a-4cc1-b1bd-8b7b25b1d31d", "fromPort":"eth0", "toPort":"eth0", "points":[62.693777028197474,225.5762388493133,62.693777028197474,235.5762388493133,-120.74357057282452,235.5762388493133,-120.74357057282452,235.5762388493133,-120.74357057282452,235.5762388493133,-120.74357057282452,225.5762388493133]},
{"from":"Switch#9b4c1d7b-9dda-49dd-a227-74d4430526c0", "to":"Switch#d047857d-020c-4829-8313-b39fe29b55de", "fromPort":"eth0", "toPort":"eth0", "points":[243.8091328874341,225.5762388493133,243.8091328874341,235.5762388493133,62.693777028197474,235.5762388493133,62.693777028197474,235.5762388493133,62.693777028197474,235.5762388493133,62.693777028197474,225.5762388493133]},
{"from":"Switch#c78e82d5-a936-4d6a-9f31-e9ee3fb5f39b", "to":"Switch#9b4c1d7b-9dda-49dd-a227-74d4430526c0", "fromPort":"eth0", "toPort":"eth0", "points":[436.53444745559614,220.93225536574312,436.53444745559614,230.93225536574312,436.53444745559614,235.5762388493133,340.1717901715151,235.5762388493133,243.8091328874341,235.5762388493133,243.8091328874341,225.5762388493133]},
{"from":"Switch#cbe82348-a333-4113-841c-456879496d4c", "to":"Switch#c78e82d5-a936-4d6a-9f31-e9ee3fb5f39b", "fromPort":"eth0", "toPort":"eth0", "points":[684.9875638266008,204.6783131732475,684.9875638266008,214.6783131732475,684.9875638266008,230.93225536574312,560.7610056410984,230.93225536574312,436.53444745559614,230.93225536574312,436.53444745559614,220.93225536574312]},
{"from":"Switch#21869922-1615-4ce5-9b2e-4ae4d91e2a74", "to":"Switch#2f2b1b88-8490-4eb1-b648-d4120fa4a4e0", "fromPort":"eth0", "toPort":"eth0", "points":[701.241506019096,439.1994790935413,701.241506019096,449.1994790935413,655.3854895026666,449.1994790935413,655.3854895026666,674.432678046695,705.8854895026666,674.432678046695,705.8854895026666,664.432678046695]},
{"from":"Switch#cbe82348-a333-4113-841c-456879496d4c", "to":"Switch#21869922-1615-4ce5-9b2e-4ae4d91e2a74", "fromPort":"eth0", "toPort":"eth0", "points":[684.9875638266008,204.6783131732475,684.9875638266008,214.6783131732475,650.741506019096,214.6783131732475,650.741506019096,449.1994790935413,701.241506019096,449.1994790935413,701.241506019096,439.1994790935413]},
{"from":"Switch#7cdb9f0d-8ec2-4e3a-85be-edb76f7ca704", "to":"Switch#cbe82348-a333-4113-841c-456879496d4c", "fromPort":"eth0", "toPort":"eth0", "points":[698.9195142773115,-39.1308197141866,698.9195142773115,-29.1308197141866,698.9195142773115,-28,740,-28,740,212,684.9875638266008,212,684.9875638266008,214.6783131732475,684.9875638266008,204.6783131732475]},
{"from":"Switch#949a0f34-eb36-4c54-a021-304e7880a246", "to":"Switch#7cdb9f0d-8ec2-4e3a-85be-edb76f7ca704", "fromPort":"eth0", "toPort":"eth0", "points":[682.6655720848155,-266.6860104091251,682.6655720848155,-256.6860104091251,682.6655720848155,-256.6860104091251,644,-256.6860104091251,644,-28,698.9195142773115,-28,698.9195142773115,-29.1308197141866,698.9195142773115,-39.1308197141866]},
{"from":"VNF#bbb332c7-ff0d-4921-87a8-534fb5892bd2", "to":"Switch#949a0f34-eb36-4c54-a021-304e7880a246", "fromPort":"eth0", "toPort":"eth0", "points":[777.9406694660858,-271.08089611645886,777.9406694660858,-261.08089611645886,777.9406694660858,-256.6860104091251,730.3031207754507,-256.6860104091251,682.6655720848155,-256.6860104091251,682.6655720848155,-266.6860104091251]},
{"from":"VNF#9ca6ad9a-1928-499a-a9ba-06f92fb60349", "to":"Switch#7cdb9f0d-8ec2-4e3a-85be-edb76f7ca704", "fromPort":"eth0", "toPort":"eth0", "points":[797.1688546670551,-42.40214976519991,797.1688546670551,-32.40214976519991,797.1688546670551,-29.1308197141866,748.0441844721834,-29.1308197141866,698.9195142773115,-29.1308197141866,698.9195142773115,-39.1308197141866]},
{"from":"VNF#5fc6d318-23a7-482c-87f2-ba79fc8ad92c", "to":"Switch#cbe82348-a333-4113-841c-456879496d4c", "fromPort":"eth0", "toPort":"eth0", "points":[809.7011471275649,186.32928235985844,809.7011471275649,196.32928235985844,809.7011471275649,214.6783131732475,747.3443554770829,214.6783131732475,684.9875638266008,214.6783131732475,684.9875638266008,204.6783131732475]},
{"from":"VNF#f435e8e7-8e6e-47c6-a976-cd151b575ffb", "to":"Switch#21869922-1615-4ce5-9b2e-4ae4d91e2a74", "fromPort":"eth0", "toPort":"eth0", "points":[830.6545964062822,430.2872989620638,830.6545964062822,440.2872989620638,830.6545964062822,444,796,444,796,452,701.241506019096,452,701.241506019096,449.1994790935413,701.241506019096,439.1994790935413]},
{"from":"VNF#1d0c699b-fd32-4f82-b908-f75910acda9b", "to":"Switch#2f2b1b88-8490-4eb1-b648-d4120fa4a4e0", "fromPort":"eth0", "toPort":"eth0", "points":[847.1180208395596,659.2785660794713,847.1180208395596,669.2785660794713,847.1180208395596,674.432678046695,776.501755171113,674.432678046695,705.8854895026666,674.432678046695,705.8854895026666,664.432678046695]},
{"from":"VNF#6b508265-6d28-4856-9cc7-ec1af3b10153", "to":"Switch#c78e82d5-a936-4d6a-9f31-e9ee3fb5f39b", "fromPort":"eth0", "toPort":"eth0", "points":[489.87304795016917,14.555458176626104,489.87304795016917,24.555458176626104,489.87304795016917,230.93225536574312,463.20374770288265,230.93225536574312,436.53444745559614,230.93225536574312,436.53444745559614,220.93225536574312]},
{"from":"VNF#06faf598-8b4b-483c-a0e2-b75c16765dc5", "to":"Switch#9b4c1d7b-9dda-49dd-a227-74d4430526c0", "fromPort":"eth0", "toPort":"eth0", "points":[304.8821918266773,17.135304380265097,304.8821918266773,27.135304380265097,304.8821918266773,235.5762388493133,274.3456623570557,235.5762388493133,243.8091328874341,235.5762388493133,243.8091328874341,225.5762388493133]},
{"from":"VNF#f39508f0-81a7-439d-942f-f77219bec86f", "to":"Switch#d047857d-020c-4829-8313-b39fe29b55de", "fromPort":"eth0", "toPort":"eth0", "points":[116.91619332468531,23.535507867504833,116.91619332468531,33.53550786750483,116.91619332468531,235.5762388493133,89.80498517644139,235.5762388493133,62.693777028197474,235.5762388493133,62.693777028197474,225.5762388493133]},
{"from":"VNF#9d518b33-0b8e-4433-8b02-2a5b4018edf4", "to":"Switch#2d3935c3-133a-4cc1-b1bd-8b7b25b1d31d", "fromPort":"eth0", "toPort":"eth0", "points":[-129.8921476424266,4.59106127430357,-129.8921476424266,14.59106127430357,-171.24357057282452,14.59106127430357,-171.24357057282452,235.5762388493133,-120.74357057282452,235.5762388493133,-120.74357057282452,225.5762388493133]},
{"from":"VNF#fb674603-49f4-4d3b-81c9-dda7aef730aa", "to":"Switch#24cec8cc-4247-4d68-9065-8f751685e0a7", "fromPort":"eth0", "toPort":"eth0", "points":[-410.64809972445585,-283.2750701194321,-410.64809972445585,-273.2750701194321,-410.64809972445585,-270.61796085983565,-357.4145089491511,-270.61796085983565,-304.1809181738464,-270.61796085983565,-304.1809181738464,-280.61796085983565]},
{"from":"VNF#612e29ac-d7f3-4c2e-880b-240eec9a4e37", "to":"Switch#ce097b94-f6ce-4995-b618-273cb5f0d837", "fromPort":"eth0", "toPort":"eth0", "points":[-422.01034753154295,-33.2575236494709,-422.01034753154295,-23.257523649470897,-301.85892643206114,-23.257523649470897,-301.85892643206114,-27.35516755272127,-301.85892643206114,-31.45281145597164,-301.85892643206114,-41.45281145597164]},
{"from":"VNF#3723cb88-7d50-495d-9c7b-1ac9ad76693b", "to":"Switch#fa3dd258-eb9d-4252-b4f9-2bd7a1b75bb4", "fromPort":"eth0", "toPort":"eth0", "points":[-413.97433678947993,207.0517897866858,-413.97433678947993,217.0517897866858,-297.21494294849117,217.0517897866858,-297.21494294849117,214.70405560907417,-297.21494294849117,212.35632143146256,-297.21494294849117,202.35632143146256]},
{"from":"VNF#5604bc84-4f12-4f89-8aed-bb3819430532", "to":"Switch#6bb109ce-52de-4de0-8e1d-8d1d7316e618", "fromPort":"eth0", "toPort":"eth0", "points":[-407.10211382783217,445.2714840120705,-407.10211382783217,455.2714840120705,-292.570959464921,455.2714840120705,-292.570959464921,451.0744856819133,-292.570959464921,446.87748735175614,-292.570959464921,436.87748735175614]},
{"from":"VNF#f8e0255a-4a3b-45e2-b66f-4700cde7f272", "to":"Switch#ffbe75b4-6ac9-4fb6-9dde-d81c6a752e80", "fromPort":"eth0", "toPort":"eth0", "points":[-398.53556783027415,676.501923713633,-398.53556783027415,686.501923713633,-299.536934690276,686.501923713633,-299.536934690276,679.3063050092715,-299.536934690276,672.1106863049099,-299.536934690276,662.1106863049099]},
{"from":"VNF#047a4503-ba57-4446-9ec7-1920f08b2693", "to":"Switch#72f5a3f8-d534-4325-b637-b1c283a669e3", "fromPort":"eth0", "toPort":"eth0", "points":[-152.83706177900427,895.6978317436656,-152.83706177900427,905.6978317436656,-102.33706177900427,905.6978317436656,-102.33706177900427,660.5007275959842,-109.13361186389909,660.5007275959842,-109.13361186389909,650.5007275959842]},
{"from":"VNF#5e078379-11fe-453c-8a64-e0f4a83c3b9f", "to":"Switch#35972182-108f-4157-af84-e1bed2d97c30", "fromPort":"eth0", "toPort":"eth0", "points":[29.30174130198543,898.173309131401,29.30174130198543,908.173309131401,81.26971096247803,908.173309131401,81.26971096247803,795.946977072618,81.26971096247803,683.7206450138351,81.26971096247803,673.7206450138351]},
{"from":"VNF#14b04bab-649a-443c-93f2-63ab8e3dc634", "to":"Switch#1c2acfd0-5e71-4490-b262-cbf462e8611a", "fromPort":"eth0", "toPort":"eth0", "points":[220.82458142469204,892.704481846706,220.82458142469204,902.704481846706,276.31701727242535,902.704481846706,276.31701727242535,793.2125634302706,276.31701727242535,683.7206450138351,276.31701727242535,673.7206450138351]},
{"from":"VNF#de6ef9e8-ebba-4766-9ec9-c722d92e37b6", "to":"Switch#3e03439d-d532-42df-ac30-c409b711f2be", "fromPort":"eth0", "toPort":"eth0", "points":[429.100948173128,892.5508385366956,429.100948173128,902.5508385366956,487.6182657748682,902.5508385366956,487.6182657748682,793.1357417752652,487.6182657748682,683.7206450138349,487.6182657748682,673.7206450138349]}
 ]}
'''

PlottingServerIPAddress = "192.168.0.18:8989"

CAR_MINIMUM_MOVEMENT_STEP = 3
CAR_MAXIMUM_MOVEMENT_STEP = 9

CAR_MINIMUM_MOVEMENT_SPEED = 5
CAR_MAXIMUM_MOVEMENT_SPEED = 19

event = Event()
AllNodes = []
CarId = 1
AllCars = {}
AllCarsToSave = {}
DataToSave = {}
expData = []


class Node:
    def __init__(self, id, neighbors, x, y, services):
        self.neighbors = neighbors
        self.id = id
        self.x = x
        self.y = y
        self.services = services

class Car:
    def __init__(self, path, speed, id, ipaddress, creationTime):
        self.path = path
        self.speed = speed
        self.currentNode = '-1'
        self.nextNode = path.split(' ')[0]
        self.id = id
        self.ipaddress = ipaddress
        self.creationTime = creationTime
        self.httperfProcessId = -1
        self.httpOptLogStr = ''
        self.isDeleted = False

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class StatusContainer:
    def __init__(self, cpu, mem, name):
        self.cpu = cpu
        self.mem = mem
        self.name = name

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class AllDataForPlotting:
    def __init__(self, allCars, allStatus, expString):
        self.allCars = allCars
        self.allStatus = allStatus
        self.expString = expString

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def disconnectContainerFromSwitch(switchName, containerName):
    str = "ovs-docker del-port " + switchName + " eth0 " + containerName
    call(str, shell=True)


def connectContainerToSwitch(switchName, containerName, ipAddress, isNewCar):
    # Find the service that is connected to the switch in order to send the traffic to it for the first time
    prefferedIpAddress = ''
    if isNewCar:
        for node in AllNodes:
            if switchName == node.id:
                prefferedIpAddress = random.choice(node.services)
        commandStr = "ovs-docker add-port " + switchName + " " + "eth0" + " " + containerName + " --ipaddress=" + ipAddress + "/24 --mtu=1400 ; docker exec " + containerName + " bash -c 'httperf --hog --server " + prefferedIpAddress + " --num-conn 60000 --num-call 10  --timeout 5 --rate 50 > httperfOptLog 2>&1 & '"
        print(commandStr)
        run(commandStr, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        commandStr = "docker exec " + containerName + " bash -c 'pidof httperf'"
        result = run(commandStr, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
        httperfPIDString = result.stdout
        for carId in AllCars:
            if carId == containerName:
                # strip function for removing the \n from the end of the PID string
                AllCars[carId].httperfProcessId = int(httperfPIDString.strip())
                break

    else:
        commandStr = "ovs-docker add-port " + switchName + " " + "eth0" + " " + containerName + " --ipaddress=" + ipAddress + "/24 --mtu=1400 ;"
        call(commandStr, shell=True)
    # call(str, shell=True)


def deleteContainer(containerName):
    for carId in AllCars:
        if carId == containerName:
            commandStr = "sudo docker exec " + containerName + " bash -c 'kill -2 " + str(AllCars[carId].httperfProcessId) + "; sleep 1 ; cat httperfOptLog'"
            result = run(commandStr, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
            AllCars[carId].httpOptLogStr = result.stdout
            break
    commandStr = "docker rm -f " + containerName
    call(commandStr, shell=True)

def changeVehicleLocation(allCarsDictionary):
    timeCounter = 1
    carToBeDeleted = []
    while True:
        if timeCounter > 20:
            timeCounter = 1
        for carId in list(allCarsDictionary):
            if not allCarsDictionary[carId].isDeleted:
                if timeCounter % allCarsDictionary[carId].speed == 0:
                    if allCarsDictionary[carId].currentNode != allCarsDictionary[carId].nextNode:
                        isNewCar = False
                        print("---------------------------------------------------")
                        print(allCarsDictionary[carId].path)
                        # Disconnect from current switch
                        if allCarsDictionary[carId].currentNode != '-1':
                            print("Disconnect vehicle <-> " + carId + " <-> to switch <-> " + allCarsDictionary[carId].currentNode)
                            disconnectContainerFromSwitch(allCarsDictionary[carId].currentNode, carId)
                        else:
                            isNewCar = True
                        if allCarsDictionary[carId].nextNode != '0':
                            # Connect to the new switch
                            allCarsDictionary[carId].currentNode = allCarsDictionary[carId].nextNode
                            connectContainerToSwitch(allCarsDictionary[carId].nextNode, carId, allCarsDictionary[carId].ipaddress, isNewCar)
                            print("Connect vehicle <-> " + carId + " <-> to switch <-> " + allCarsDictionary[carId].nextNode)
                            nodeIndexInArray = (allCarsDictionary[carId].path.split(" ")).index(allCarsDictionary[carId].currentNode)
                            allCarsDictionary[carId].nextNode = (allCarsDictionary[carId].path.split(' '))[nodeIndexInArray + 1]
                        else:
                            carToBeDeleted.append(carId)

        if len(carToBeDeleted) > 0:
            for mustDeleteCar in carToBeDeleted:
                deleteContainer(mustDeleteCar)
                allCarsDictionary[mustDeleteCar].isDeleted = True
                print("Delete vehicle " + mustDeleteCar)
                # Dont delete the car from the history if not use "allCarsDictionary.pop(mustDeleteCar)"
            carToBeDeleted = []



        timeCounter += 1
        if event.is_set():
            break
        time.sleep(1)

def showDistribution(values):
    pass
# sns.distplot(values, hist=False)
# plt.show()




if __name__ == '__main__':
    NumberOfCars = 0
    OutputFileName = ""
    InputFileName = ""
    lmd = 5
    plotProcess = None

    parser = ArgumentParser()
    parser.add_argument("-o", "--output", dest="outputFileName",
                        help="Output file name")
    parser.add_argument("-l", "--load", dest="loadSavedData",
                        help="Name of saved data to be loaded")
    parser.add_argument("-n", "--number", dest="number",
                        help="Number of vehicles")
    parser.add_argument("-L", "--lambda", dest="lmd",
                        help="Lambda for exponential distribution")

    args = parser.parse_args()
    if args.number:
        NumberOfCars = int(args.number)
    else:
        NumberOfCars = 10
    if args.outputFileName:
        OutputFileName = args.outputFileName
    else:
        OutputFileName = "AllCarsSavedData.json"
    if args.loadSavedData:
        InputFileName = args.loadSavedData
    else:
        InputFileName = ""
    if args.lmd:
        lmd = int(args.lmd)
    else:
        lmd = 5


    # Start a thread to move containert between switches
    t = Thread(target=changeVehicleLocation, args=(AllCars, ))
    t.start()

    if InputFileName:
        rawDataFromFile = ""
        temp = []
        with open(InputFileName) as f:
            rawDataFromFile = json.load(f)

        for carId in rawDataFromFile:
            temp.append(rawDataFromFile[carId])

        for vehicle in temp:
            car = Car(vehicle['path'], int(vehicle['speed']), vehicle['id'], vehicle['ipaddress'])
            dockerRunCommand = "sudo docker run -dit --net=none --name=" + vehicle['id'] + " nephilimboy/vehicle:v4"
            print("Car created")
            print(dockerRunCommand)
            time.sleep(vehicle['creationTime'])
            call(dockerRunCommand, shell=True)
            AllCars[car.id] = car

    else:
        # Converting the Json data to obj on nodes
        data = json.loads(Topology)
        for nodeId in data['nodeDataArray']:
            if nodeId['name'] == "Switch":
                node = Node(((nodeId['describtion']).split('#')[1]), [], 0, 0, [])
                nodeNeighbors = []
                servicesID = []
                connectedServicesIp = []
                for link in data['linkDataArray']:
                    # Switch <-> switch
                    if link['from'].split('#')[0] == "Switch" and link['to'].split('#')[0] == "Switch":
                        if (link['from']).split('-')[1] == node.id:
                            nodeNeighbors.append((link['to']).split('-')[1])
                        elif (link['to']).split('-')[1] == node.id:
                            nodeNeighbors.append((link['from']).split('-')[1])
                    # Switch <-> VNF (service)
                    else:
                        if (link['from']).split('-')[1] == node.id:
                            servicesID.append((link['to']).split('-')[1])
                        elif (link['to']).split('-')[1] == node.id:
                            servicesID.append((link['from']).split('-')[1])

                # Find the IP address of the services
                for servicesIDNum in data['nodeDataArray']:
                    if servicesIDNum['name'] == "VNF":
                        for connectedServices in servicesID:
                            if (servicesIDNum['describtion']).split('#')[1] == connectedServices:
                                connectedServicesIp.append((servicesIDNum['bottomArray'][0])['ipAddress'])
                                break

                node.neighbors = nodeNeighbors
                node.services = connectedServicesIp
                AllNodes.append(node)

        # Create a container and push it to the queue
        expIntigerArray = npRand.exponential(scale=lmd, size=NumberOfCars)
        for floatData in expIntigerArray:
            expData.append(str(floatData))
        print("#########################")
        print("EXP distribution: ")
        print(expIntigerArray)
        print("#########################")
        for x in range(NumberOfCars):
            CarId = CarId + 1
            previousNode = ''
            path = []
            currentNode = random.choice(AllNodes)
            path.append(currentNode.id)
            try:
                for i in range(random.randint(CAR_MINIMUM_MOVEMENT_STEP, CAR_MAXIMUM_MOVEMENT_STEP)):
                    if len(currentNode.neighbors) > 1:
                        nextNodeId = ''
                        while True:
                            nextNodeId = random.choice(currentNode.neighbors)
                            if nextNodeId != previousNode:
                                break
                        path.append(nextNodeId)
                        # Find the next node object
                        previousNode = currentNode.id
                        for tempNode in AllNodes:
                            if tempNode.id == nextNodeId:
                                currentNode = tempNode
                path.append('0')
                str2 = ''
                for sw in path:
                    str2 = str2 + sw + " "

                # dockerRunCommand = "sudo docker run -dit --net=none --name=car" + f'{CarId}' + " nephilimboy/vehicle:v4 bash -c '" + "echo 10.10.10." + f'{CarId}' + " > ipddr; bash StartTheCar.sh " + str + "' "
                # dockerRunCommand = "sudo docker run -dit --net=none --name=car" + str(CarId) + " nephilimboy/vehicle:v4 bash -c '" + "echo 10.10.10." + str(CarId) + " > ipddr; bash StartTheCar.sh " + str2 + "' "


                dockerRunCommand = "sudo docker run -dit --net=none --name=car" + str(CarId) + " nephilimboy/httperf_fdsize100k_python_v2"
                call(dockerRunCommand, shell=True)

                speed = random.randint(CAR_MINIMUM_MOVEMENT_SPEED, CAR_MAXIMUM_MOVEMENT_SPEED)
                print("----------------------------------------------------------")
                print("[*] Car: ")
                print("     -> ID: " + "car" + str(CarId))
                print("     -> speed: " + str(speed))
                print("     -> IP address: " + "10.10.10." + str(CarId))
                print("     -> creation time: " + str(round(expIntigerArray[x], 1)))
                print("     -> route: " + str2)
                time.sleep(round(expIntigerArray[x], 1))

                AllCars["car" + str(CarId)] = Car(str2, speed, "car" + str(CarId), "10.10.10." + str(CarId), round(expIntigerArray[x], 1))
                # No changes will happen for the current node and so on during the saving process
                AllCarsToSave["car" + str(CarId)] = Car(str2, speed, "car" + str(CarId), "10.10.10." + str(CarId), round(expIntigerArray[x], 1))
                print("[*] Car has been deployed")

            except KeyboardInterrupt:
                event.set()
                break

    while True:
        emulationFinished = True
        for vehicleID in AllCars:
            if not AllCars[vehicleID].isDeleted:
                emulationFinished = False
                break
        if emulationFinished:
            containerArray = []
            AllStatus = {}
            with open("./allContainerStats") as file:
                for line in file:
                    if line.startswith("----------------------------------------"):
                        time = (line.split())[4]
                        if len(containerArray) > 0:
                            AllStatus[time] = containerArray
                            containerArray = []
                    elif not line.startswith("CONTAINER"):
                        if len(line.split()) > 6:
                            containerArray.append(StatusContainer(((line.split())[2]).replace("%", ""), ((line.split())[6]).replace("%", ""), ((line.split())[1])))
            ###################################
            json_object = json.dumps(AllDataForPlotting(AllCars, AllStatus, expData), indent = 5, default=lambda x: x.__dict__)
            print(json_object)
            requests.post('http://' + PlottingServerIPAddress, data = json_object)
            ###################################
            t.join()

            event.set()
            break


