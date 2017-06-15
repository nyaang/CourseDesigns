#include "stdafx.h"
#include <iostream>
using namespace std;

typedef struct CTNODE {
	double cost; //存放个人经费消耗
	int person_num;	//记录是第几人的选择层，值等于当前结点所在层次数-1
	int task_num; //记录是第几个任务，值等于母结点的从左往右的第几个子结点数
	int task_finished;	//记录已经完成多少任务
	int travellist[13];	//记录是遍历过哪些任务，遍历的时候会用上
	double allcost; //记录总的费用，遍历的时候会用上
	CTNODE* child; //子结点
};

//创建并初始化树，给所有结点的person_num,task_num赋值，travellist中的值初始化为-1
void createchildnode(CTNODE& parnode, int m, int n) {
	if (parnode.person_num < n) {
		parnode.child = new CTNODE[m + 1];
		for (int i = 0; i <= m; i++) {
			parnode.child[i].person_num = parnode.person_num + 1;
			parnode.child[i].task_num = i;
			parnode.child[i].task_finished = 0;
			//parnode.child[i].travellist = new int[n + 1];
			for (int j = 0; j <= 12; j++) {
				parnode.child[i].travellist[j] = -1;
			}
			createchildnode(parnode.child[i], m, n);
		}
	}
}

//遍历树
void inittree(CTNODE& parnode, double(&cost)[12][12], int n, int m, CTNODE* leafnode, int& leafnum) {	//需要提供一个根节点的引用，cost矩阵,n,m，存储结果的的矩阵，方案数
	bool travelvalue = 1;	//辅助变量，用于判断是否需要遍历该结点
	if (parnode.task_finished < m) {
		if (parnode.person_num < n) {
			for (int i = 0; i <= m; i++) {
				for (int j = 1; j <= n; j++) {
					//如果子结点的task_num已经出现在母结点的travelist中，则不遍历该结点
					if (parnode.child[i].task_num != 0) {
						if (parnode.child[i].task_num == parnode.travellist[j]) {
							travelvalue = 0;
						}
					}
				}
				if (travelvalue == 1) {
					parnode.child[i].cost = cost[parnode.child[i].person_num][parnode.child[i].task_num];
					parnode.child[i].task_finished = parnode.task_finished;
					if (parnode.child[i].cost != 0) { parnode.child[i].task_finished = parnode.task_finished + 1; }	//代表该人不分配任务
					parnode.child[i].allcost = parnode.allcost + parnode.child[i].cost;
					for (int k = 0; k < parnode.child[i].person_num; k++) {
						parnode.child[i].travellist[k] = parnode.travellist[k];
					}

					parnode.child[i].travellist[parnode.child[i].person_num] = parnode.child[i].task_num;
					inittree(parnode.child[i], cost, n, m, leafnode, leafnum);
				}
				travelvalue = 1;
			}
		}

	}
	//含有结果结点的情况，存入辅助ctnode数组
	if (parnode.task_finished == m) {
		leafnum++;
		leafnode[leafnum] = parnode;
	}
}

//求最小值，目前只输出一个最小值
void sortcost(CTNODE* leafnode, int leafnum, int n) {
	CTNODE minleaf = leafnode[1];	//辅助变量，存放最优解
	for (int i = 2; i <= leafnum; i++) {
		if (minleaf.allcost > leafnode[i].allcost) {
			minleaf = leafnode[i];
		}
	}
	//结果输出，循环中的第X次cout输出的值代表第X人做的任务编号
	cout << minleaf.allcost << endl;
	for (int j = 1; j <= n; j++) {
		cout << minleaf.travellist[j]<<" ";
	}
}

//求阶乘工具
int jiecheng(int x) {
	int mul = 1;
	for (x; x >= 1; x--) {
		mul = mul*x;
	}
	return mul;
}

int main()
{
	//n个人，m个任务
	CTNODE rootnode;
	double cost[12][12];	//12是我设置的上限，可随需求调高
	int m, n;
	cin >> n; cin >> m;
	int i, j;
	for (i = 1; i <= n; i++) {	
		cost[i][0] = 0;	//第0个任务含义为不做任务，cost值为0
	}
	for (i = 1; i <= n; i++)
	{
		//for (j = 1; j <= m; j++){
		//	cin >> cost[i][j];
		//}
		cin >> cost[i][1] >> cost[i][2] >> cost[i][3]>> cost[i][4] >> cost[i][5] >> cost[i][6]>> cost[i][7];	//针对7个任务的输入格式
	}
	rootnode.cost = 0; rootnode.person_num = 0; rootnode.task_num = -2; rootnode.allcost = 0; rootnode.task_finished = 0;	//根结点的数据成员无实际意义
	//rootnode.travellist = new int[n + 1];
	for (int i = 0; i <= 12; i++) {
		rootnode.travellist[i] = -2;	
	}
	createchildnode(rootnode, m, n);
	int leafsize = jiecheng(m)*jiecheng(n) / (jiecheng(n - m)*jiecheng(m));
	leafsize = leafsize + 1;
	CTNODE* leafnode = new CTNODE[leafsize];	//辅助CTNODE数组，存放所有的代表结果的结点
	int leafnum = 0;	//辅助变量，记录CTNODE中有多少个代表结果的结点

	inittree(rootnode, cost, n, m, leafnode, leafnum);
	sortcost(leafnode, leafnum, n);
	system("pause");
	return 0;
}
