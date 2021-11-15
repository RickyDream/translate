# -*- coding: utf-8 -*-
# __author__ : Ricky
# __createTime__ : 2021/1/21 11:17
# __fileName__ : GoldenCoordinateV2 TreeMap.py
# __devIDE__ : PyCharm
from Utils.OrganizationNode.DepartMap import DepartMap
from Utils.OrganizationNode.Depart import Depart
from Utils.OrganizationNode.Employee import Employee
import copy




class TreeMap():
    def __init__(self, data):
        super().__init__()
        self.data = data


    def setData(self, data):
      self.data = data
    def getDepartArch(self):
        self.departArch = {}
        departMap = DepartMap()
        dat = copy.deepcopy(self.data)
        if dat.get('child'):
            child = dat.pop('child')
            _id = dat['pid']
            self.departArch.setdefault(_id, departMap)
            self._getDepartArch(child, departMap)
        return self.departArch


    def _getDepartArch(self, data, departMap):

        for dat in data:

            type = dat.get('type')
            if type == 'department':
                _id = dat['id']
                _departMap = DepartMap()
                self.departArch.setdefault(_id, _departMap)
                if dat.get('child'):
                    child = dat.pop('child')
                    depart = Depart(dat)
                    departMap.addChildDepart(depart)
                    self._getDepartArch(child, _departMap)
                else:
                    depart = Depart(dat)
                    departMap.addChildDepart(depart)
            else:
                emp = Employee(dat)
                departMap.addMember(emp)
treeMap = TreeMap(None)
if __name__ == '__main__':
    null = None
    dic = {
      "errcode": 0,
      "errmsg": "ok",
      "data": {
        "name": "公司根目录",
        "pid": 1,
        "id": 298,
        "avatar": null,
        "type": "department",
        "child": [
          {
            "job_number": 2354,
            "name": null,
            "phone": "14551753072",
            "user_id": 18930,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2359,
            "name": null,
            "phone": "15884833688",
            "user_id": 19128,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2360,
            "name": null,
            "phone": "18261531647",
            "user_id": 19015,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2361,
            "name": null,
            "phone": "13866330193",
            "user_id": 19112,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2362,
            "name": null,
            "phone": "15954792843",
            "user_id": 19101,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2363,
            "name": null,
            "phone": "13677616664",
            "user_id": 19003,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2364,
            "name": null,
            "phone": "18526412280",
            "user_id": 19232,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2365,
            "name": null,
            "phone": "13929216381",
            "user_id": 19053,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2366,
            "name": null,
            "phone": "18517684255",
            "user_id": 19210,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2367,
            "name": null,
            "phone": "14520792905",
            "user_id": 18981,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2368,
            "name": null,
            "phone": "13377555414",
            "user_id": 19051,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2369,
            "name": null,
            "phone": "15754279040",
            "user_id": 19025,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2370,
            "name": null,
            "phone": "13851788402",
            "user_id": 19077,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2371,
            "name": null,
            "phone": "13289994926",
            "user_id": 19152,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2372,
            "name": null,
            "phone": "15903927325",
            "user_id": 19233,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2373,
            "name": null,
            "phone": "15801919077",
            "user_id": 19073,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2374,
            "name": null,
            "phone": "13356213675",
            "user_id": 19134,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2375,
            "name": null,
            "phone": "15879914278",
            "user_id": 19214,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2376,
            "name": null,
            "phone": "14705365163",
            "user_id": 19075,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2377,
            "name": null,
            "phone": "15271481081",
            "user_id": 19157,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2378,
            "name": null,
            "phone": "14563363495",
            "user_id": 19010,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2379,
            "name": null,
            "phone": "15292153503",
            "user_id": 18974,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2380,
            "name": null,
            "phone": "15620331551",
            "user_id": 18942,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2381,
            "name": null,
            "phone": "14559482271",
            "user_id": 19082,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2382,
            "name": null,
            "phone": "15836415740",
            "user_id": 18979,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2383,
            "name": null,
            "phone": "18004903536",
            "user_id": 19090,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2384,
            "name": null,
            "phone": "15039964638",
            "user_id": 19186,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2385,
            "name": null,
            "phone": "13062353083",
            "user_id": 19009,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2386,
            "name": null,
            "phone": "13227599743",
            "user_id": 19159,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2387,
            "name": null,
            "phone": "18142951195",
            "user_id": 19170,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2388,
            "name": null,
            "phone": "15690489819",
            "user_id": 19172,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2389,
            "name": null,
            "phone": "13391981473",
            "user_id": 19219,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2390,
            "name": null,
            "phone": "15874734795",
            "user_id": 19180,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2391,
            "name": null,
            "phone": "13839779291",
            "user_id": 19036,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2392,
            "name": null,
            "phone": "14580675860",
            "user_id": 19017,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2393,
            "name": null,
            "phone": "13994942657",
            "user_id": 19012,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2394,
            "name": null,
            "phone": "15947894126",
            "user_id": 19204,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2395,
            "name": null,
            "phone": "18527161249",
            "user_id": 18972,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2396,
            "name": null,
            "phone": "15505631626",
            "user_id": 18939,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2397,
            "name": null,
            "phone": "15785444474",
            "user_id": 19068,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2398,
            "name": null,
            "phone": "18696444404",
            "user_id": 19126,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2399,
            "name": null,
            "phone": "15365011944",
            "user_id": 19168,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2400,
            "name": null,
            "phone": "14539869107",
            "user_id": 19056,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2401,
            "name": null,
            "phone": "18160884704",
            "user_id": 19194,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2402,
            "name": null,
            "phone": "15086045535",
            "user_id": 19064,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2403,
            "name": null,
            "phone": "18839996785",
            "user_id": 18968,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2404,
            "name": null,
            "phone": "18798868069",
            "user_id": 19146,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2405,
            "name": null,
            "phone": "13464189310",
            "user_id": 19026,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2406,
            "name": null,
            "phone": "13594515714",
            "user_id": 19205,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2407,
            "name": null,
            "phone": "15091364766",
            "user_id": 18973,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2408,
            "name": null,
            "phone": "13798643538",
            "user_id": 19131,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2409,
            "name": null,
            "phone": "13297784077",
            "user_id": 19106,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2410,
            "name": null,
            "phone": "13071109791",
            "user_id": 19129,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2411,
            "name": null,
            "phone": "13496403872",
            "user_id": 18954,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2412,
            "name": null,
            "phone": "13818691019",
            "user_id": 19070,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2413,
            "name": null,
            "phone": "15109141855",
            "user_id": 19130,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2414,
            "name": null,
            "phone": "13404009437",
            "user_id": 19148,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2415,
            "name": null,
            "phone": "15265063866",
            "user_id": 19037,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2416,
            "name": null,
            "phone": "18155277619",
            "user_id": 19006,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2417,
            "name": null,
            "phone": "13369892563",
            "user_id": 19122,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2418,
            "name": null,
            "phone": "18570912548",
            "user_id": 19014,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2419,
            "name": null,
            "phone": "18747438269",
            "user_id": 19039,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2420,
            "name": null,
            "phone": "14557801108",
            "user_id": 19236,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2421,
            "name": null,
            "phone": "15071435225",
            "user_id": 19005,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2422,
            "name": null,
            "phone": "15782826124",
            "user_id": 19239,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2423,
            "name": null,
            "phone": "15800648001",
            "user_id": 19093,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2424,
            "name": null,
            "phone": "18848022387",
            "user_id": 19123,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2425,
            "name": null,
            "phone": "13195905211",
            "user_id": 19163,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2426,
            "name": null,
            "phone": "14710686956",
            "user_id": 18997,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2427,
            "name": null,
            "phone": "13585485169",
            "user_id": 19227,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2428,
            "name": null,
            "phone": "15289945579",
            "user_id": 18955,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2429,
            "name": null,
            "phone": "14714359786",
            "user_id": 19185,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2430,
            "name": null,
            "phone": "18563919163",
            "user_id": 19156,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2431,
            "name": null,
            "phone": "15062258438",
            "user_id": 18991,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2432,
            "name": null,
            "phone": "18820562734",
            "user_id": 18980,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2433,
            "name": null,
            "phone": "13963098241",
            "user_id": 19145,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2434,
            "name": null,
            "phone": "15343743554",
            "user_id": 19099,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2435,
            "name": null,
            "phone": "13762455311",
            "user_id": 19004,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2436,
            "name": null,
            "phone": "13880679150",
            "user_id": 19241,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2437,
            "name": null,
            "phone": "14508055842",
            "user_id": 19096,
            "avatar": null,
            "type": "emp"
          },
          {
            "job_number": 2438,
            "name": null,
            "phone": "15901748395",
            "user_id": 19161,
            "avatar": null,
            "type": "emp"
          },
          {
            "name": "产品部",
            "pid": 298,
            "id": 303,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2412,
                "name": null,
                "phone": "13818691019",
                "user_id": 19070,
                "avatar": null,
                "type": "emp"
              }
            ]
          },
          {
            "name": "设计部",
            "pid": 298,
            "id": 304,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2434,
                "name": null,
                "phone": "15343743554",
                "user_id": 19099,
                "avatar": null,
                "type": "emp"
              }
            ]
          },
          {
            "name": "技术部",
            "pid": 298,
            "id": 305,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2362,
                "name": null,
                "phone": "15954792843",
                "user_id": 19101,
                "avatar": null,
                "type": "emp"
              },
              {
                "name": "前端部",
                "pid": 305,
                "id": 306,
                "avatar": null,
                "type": "department",
                "child": [
                  {
                    "job_number": 2362,
                    "name": null,
                    "phone": "15954792843",
                    "user_id": 19101,
                    "avatar": null,
                    "type": "emp"
                  }
                ]
              },
              {
                "name": "后端部",
                "pid": 305,
                "id": 307,
                "avatar": null,
                "type": "department",
                "child": [
                  {
                    "job_number": 2362,
                    "name": null,
                    "phone": "15954792843",
                    "user_id": 19101,
                    "avatar": null,
                    "type": "emp"
                  }
                ]
              },
              {
                "name": "测试部",
                "pid": 305,
                "id": 308,
                "avatar": null,
                "type": "department",
                "child": [
                  {
                    "job_number": 2362,
                    "name": null,
                    "phone": "15954792843",
                    "user_id": 19101,
                    "avatar": null,
                    "type": "emp"
                  }
                ]
              },
              {
                "name": "运维部",
                "pid": 305,
                "id": 309,
                "avatar": null,
                "type": "department",
                "child": [
                  {
                    "job_number": 2362,
                    "name": null,
                    "phone": "15954792843",
                    "user_id": 19101,
                    "avatar": null,
                    "type": "emp"
                  }
                ]
              },
              {
                "name": "数据部",
                "pid": 305,
                "id": 310,
                "avatar": null,
                "type": "department",
                "child": [
                  {
                    "job_number": 2362,
                    "name": null,
                    "phone": "15954792843",
                    "user_id": 19101,
                    "avatar": null,
                    "type": "emp"
                  }
                ]
              }
            ]
          },
          {
            "name": "运营部",
            "pid": 298,
            "id": 311,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2386,
                "name": null,
                "phone": "13227599743",
                "user_id": 19159,
                "avatar": null,
                "type": "emp"
              }
            ]
          },
          {
            "name": "品牌部",
            "pid": 298,
            "id": 312,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2427,
                "name": null,
                "phone": "13585485169",
                "user_id": 19227,
                "avatar": null,
                "type": "emp"
              }
            ]
          },
          {
            "name": "人力部",
            "pid": 298,
            "id": 313,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2387,
                "name": null,
                "phone": "18142951195",
                "user_id": 19170,
                "avatar": null,
                "type": "emp"
              }
            ]
          },
          {
            "name": "行政部",
            "pid": 298,
            "id": 314,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2422,
                "name": null,
                "phone": "15782826124",
                "user_id": 19239,
                "avatar": null,
                "type": "emp"
              }
            ]
          },
          {
            "name": "财务部",
            "pid": 298,
            "id": 315,
            "avatar": null,
            "type": "department",
            "child": [
              {
                "job_number": 2395,
                "name": null,
                "phone": "18527161249",
                "user_id": 18972,
                "avatar": null,
                "type": "emp"
              }
            ]
          }
        ]
      }
    }
    treeMap = TreeMap(dic['data'])
    print(treeMap.getDepartArch())

